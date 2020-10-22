from flask_restful import Resource, request
from flask import make_response

from src.config import ApiConfig, APIMethod
from src.user.user import reset_password, change_password, verify_user_code, forget_change_password


class ResetPassword(Resource):
    def post(self):
        data, response = reset_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


def forgetpassword(app):
    @app.route('{prefix}/v{version}/forgetpassword'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def forgetpassword_api():
        data, response = reset_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


def user_verify_code(app):
    @app.route('{prefix}/v{version}/forgetpassword/verifycode'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def user_verify_code_api():
        data, response = verify_user_code(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


def forget_password_change(app):
    @app.route('{prefix}/v{version}/forgetpassword/changepassword'
               .format(prefix=app.config[ApiConfig.REST_URL_PREFIX],
                       version=app.config[ApiConfig.API_VERSION]), methods=[APIMethod.POST])
    def verify_code_api():
        data, response = forget_change_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


class ChangePassword(Resource):
    def post(self):
        data, response = change_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)
