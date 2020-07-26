from flask_restful import Resource
from flask import make_response

from src.config import ApiConfig
from src.http import http


class Logout(Resource):
    def post(self):
        data = {}
        data[ApiConfig.DATA] = 'Successfully Logout'
        return make_response(data, http.HTTP_OK)