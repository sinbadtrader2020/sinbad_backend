from flask import request, abort, jsonify, make_response

from src.config import ApiConfig, UserConfig, APIMethod
from src.dbapi import insert_query
from src.http import http


def subscribe_user(app):
    @app.route('{prefix}/v{version}/subscribe'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def subscribe_user_api():
        data = {}

        if UserConfig.EMAIL not in request.json:
            data[ApiConfig.MESSAGE] = "Email Missing"
            return make_response(jsonify(data), http.HTTP_NOT_ACCEPTABLE)

        result, success = insert_query.insert_subscribe_user(request.json)

        email = request.json.get(UserConfig.EMAIL)
        if success:
            data[ApiConfig.MESSAGE] = 'Thanks for subscribing! ' + email + \
                                      ' has been added to our mailing list.'
        else:
            data[ApiConfig.MESSAGE] = 'Already ' + email + ' has been added to our mailing list.'

        return make_response(jsonify(data), http.HTTP_OK)