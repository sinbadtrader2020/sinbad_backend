from flask import request, abort, jsonify, make_response
from itsdangerous import (TimedJSONWebSignatureSerializer as
                          Serializer, BadSignature, SignatureExpired)

from src.config import ApiConfig, UserConfig, APIMethod
from src.dbapi import insert_query, get_query
from src.http import http
from src.utils import helperfunction
from src.token.config import Payload
from src.token import jwt_parser


class CustomException(Exception):
   """Base class for other exceptions"""
   pass


def generate_auth_token(id, app, expiration=600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': id})


def signup(app):

    @app.route('{prefix}/v{version}/signup'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def signup_api():
        email       = request.json.get(UserConfig.EMAIL)
        password    = request.json.get(UserConfig.PASSWORD)
        if email is None or password is None:
            abort(http.HTTP_BAD_REQUEST)  # missing arguments

        success = False
        data = None

        # print(username, " ", password)
        request.json[UserConfig.USERCREATETIME] = helperfunction.get_current_date_and_time()
        data, success = insert_query.insert_user(request.json)

        if success and data and data[ApiConfig.DATA]:
            data, success = get_query.get_user_by_id(data[ApiConfig.DATA][0].get(ApiConfig.ID))
            print(data, '--->', success)
            t = helperfunction.get_current_date_and_time()

            payload = {
                Payload.AUDIENCE: app.config.get('SERVICE_ID'),
                Payload.ISSUER: app.config.get('APPLICATION_ID'),
                Payload.SUBJECT: app.config.get('DOMAIN'),
                Payload.EXPIRATION: t,
                UserConfig.EMAIL: email,
            }

            try:
                response = jwt_parser.get_token(payload=payload, secret=app.config.get('SECRET_KEY'))
                data[ApiConfig.TOKEN] = response
            except CustomException:
                print("This value is too small, try again!")
            return make_response(jsonify(data), http.HTTP_CREATED)

        return http.get_response(data, success, http.POST, http.HTTP_CONFLICT)
