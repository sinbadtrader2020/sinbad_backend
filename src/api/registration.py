from flask import request, abort, jsonify, make_response
from itsdangerous import (TimedJSONWebSignatureSerializer as
                          Serializer, BadSignature, SignatureExpired)

from src.config import ApiConfig, UserConfig, APIMethod
from src.dbapi import insert_query, get_query
from src.http import http
from src.utils import helperfunction


def generate_auth_token(id, app, expiration=600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': id})


def registration(app):

    @app.route('{prefix}/v{version}/registration'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def registration_api():
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
            return make_response(jsonify(data), http.HTTP_CREATED)

        return http.get_response(data, success, http.POST, http.HTTP_CONFLICT)
