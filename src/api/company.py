from flask_restful import Resource, request
from flask import make_response

from src.dbapi import get_query, update_query
from src.http import http


class CompanyList(Resource):
    def get(self):
        data, success = get_query.get_company_details()
        return make_response(data, http.HTTP_OK)


class Company(Resource):
    def get(self, id):
        data, success = get_query.get_company_details(symbol=id)
        return make_response(data, http.HTTP_OK)
