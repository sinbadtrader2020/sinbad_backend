from flask_restful import Resource, request
from flask import make_response

from src.config import ApiConfig
from src.user.user import reset_password, change_password


class ResetPassword(Resource):
    def post(self):
        data, response = reset_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


class ForgetPassword(Resource):
    def post(self):
        data, response = reset_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)


class ChangePassword(Resource):
    def post(self):
        data, response = change_password(request.json)
        message = {ApiConfig.MESSAGE: data}
        return make_response(message, response)
