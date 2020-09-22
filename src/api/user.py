from flask_restful import Resource, request
from flask import make_response

from src.config import ApiConfig
from src.dbapi import get_query, update_query
from src.http import http


class UserList(Resource):
    def get(self):
        data, success = get_query.get_all_user()
        return make_response(data, http.HTTP_OK)


class User(Resource):
    def get(self, id):
        data, success = get_query.get_user_by_id(id)
        return make_response(data, http.HTTP_OK)

    def post(self, id):
        data, success = update_query.update_user(request.json, id)
        return make_response(data, http.HTTP_OK)