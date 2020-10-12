from flask import request, abort, jsonify, make_response

from src.config import ApiConfig, UserConfig, APIMethod
from src.dbapi import insert_query
from src.http import http


def get_app_url_user(app):
    @app.route('{prefix}/v{version}/get_app_url'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def get_app_url_user_api():
        data = {}

        if UserConfig.MOBILE_NUMBER not in request.json:
            data[ApiConfig.MESSAGE] = "Mobile Missing"
            return make_response(jsonify(data), http.HTTP_NOT_ACCEPTABLE)

        result, success = insert_query.insert_get_app_url_user(request.json)
        mobile_number = request.json.get(UserConfig.MOBILE_NUMBER)
        data[ApiConfig.MESSAGE] = 'Send' + mobile_number + ' subscriber Now'

        return make_response(jsonify(data), http.HTTP_OK)