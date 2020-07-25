from flask import request, abort, jsonify, make_response
from itsdangerous import (TimedJSONWebSignatureSerializer as
                          Serializer, BadSignature, SignatureExpired)

from src.config import ApiConfig, UserConfig, APIMethod
from src.dbconn import query, dbname
from src.http.http import HTTP_OK, HTTP_BAD_REQUEST, HTTP_UNAUTHORIZED
from src.utils import helperfunction


def generate_auth_token(id, app, expiration=600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': id})


def login(app):
    admin_user = ApiConfig.ADMIN
    admin_passwd = app.config[ApiConfig.ADMIN_PASSWORD]

    @app.route('{prefix}/v{version}/login'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def login_api():
        email       = request.json.get(UserConfig.EMAIL)
        password    = request.json.get(UserConfig.PASSWORD)
        if email is None or password is None:
            abort(HTTP_BAD_REQUEST)  # missing arguments

        success = False
        data = None
        if email == admin_user:
            if password == admin_passwd:
                success = True
                data = {
                    ApiConfig.DATA: [
                        {
                            "user": "admin"
                        }
                    ]
                }
        else:
            field_value = [UserConfig.EMAIL]
            offset_value = [email]

            # print(username, " ", password)
            data, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE, field_name=field_value,
                                       offset=offset_value, qparam=True)

            if success and data and data[ApiConfig.DATA]:
                if data.get(ApiConfig.DATA)[0].get(UserConfig.PASSWORD) == password:
                    data, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE_VIEW,
                                                     field_name=field_value,
                                                     offset=offset_value, qparam=True)
                else:
                    success = False

        if success and data and data[ApiConfig.DATA]:
            return make_response(jsonify(data), HTTP_OK)

        data = {}
        data[ApiConfig.ERROR] = data if (data and data.get(ApiConfig.ERROR)) else 'Unauthorized'
        data[ApiConfig.MESSAGE] = "Invalid Username and Password."

        return make_response(jsonify(data), HTTP_UNAUTHORIZED)
