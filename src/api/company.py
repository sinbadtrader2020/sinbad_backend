from flask_restful import Resource, request
from flask import make_response

from src.config import CompliantConfig
from src.dbapi import get_query
from src.http import http


class CompanyList(Resource):
    def get(self):
        data, success = get_query.get_company_details()
        return make_response(data, http.HTTP_OK)


class Company(Resource):
    def get(self, id):
        data, success = get_query.get_company_details(symbol=id)
        return make_response(data, http.HTTP_OK)


class CompliantCompanyList(Resource):
    def get(self):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.COMPLIANT)
        return make_response(data, http.HTTP_OK)


class CompliantCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.COMPLIANT,
                                                                     symbol=id)
        return make_response(data, http.HTTP_OK)


class NonCompliantCompanyList(Resource):
    def get(self):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.NONCOMPLIANT)
        return make_response(data, http.HTTP_OK)


class NonCompliantCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.NONCOMPLIANT,
                                                                     symbol=id)
        return make_response(data, http.HTTP_OK)


class YellowCompanyList(Resource):
    def get(self):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.YELLOW)
        return make_response(data, http.HTTP_OK)


class YellowCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.YELLOW, symbol=id)
        return make_response(data, http.HTTP_OK)
