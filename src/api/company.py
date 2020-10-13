from flask_restful import Resource, request
from flask import make_response

from src.config import ApiConfig, CompliantConfig
from src.dbapi import get_query
from src.http import http


class CompanyList(Resource):
    def get(self):
        limit = request.args.get(ApiConfig.LIMIT, default=0, type=int)
        offset = request.args.get(ApiConfig.OFFSET, default=0, type=int)

        data, success = get_query.get_company_details(limit=limit, offset=offset)

        result, success = get_query.get_company_number()
        count = 0

        if len(result.get(ApiConfig.DATA)):
            count = result.get(ApiConfig.DATA)[0].get(ApiConfig.COUNT)
            data[ApiConfig.TOTAL_ITEM] = count

        if len(data.get(ApiConfig.DATA)) and limit:
            length = len(data.get(ApiConfig.DATA))
            next_offset = length + offset
            if count <=next_offset:
                next_offset = 0
            data[ApiConfig.NEXT_OFFSET] = next_offset

        return make_response(data, http.HTTP_OK)


class Company(Resource):
    def get(self, id):
        data, success = get_query.get_company_details(symbol=id)
        return make_response(data, http.HTTP_OK)


class CompliantCompanyList(Resource):
    def get(self):
        limit = request.args.get(ApiConfig.LIMIT, default=0, type=int)
        offset = request.args.get(ApiConfig.OFFSET, default=0, type=int)

        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.COMPLIANT,
                                                                     limit=limit, offset=offset)

        result, success = get_query.get_company_number(CompliantConfig.COMPLIANT)
        count = 0

        if len(result.get(ApiConfig.DATA)):
            count = result.get(ApiConfig.DATA)[0].get(ApiConfig.COUNT)
            data[ApiConfig.TOTAL_ITEM] = count

        if len(data.get(ApiConfig.DATA)) and limit:
            length = len(data.get(ApiConfig.DATA))
            next_offset = length + offset
            if count <=next_offset:
                next_offset = 0
            data[ApiConfig.NEXT_OFFSET] = next_offset

        return make_response(data, http.HTTP_OK)


class CompliantCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.COMPLIANT,
                                                                     symbol=id)
        return make_response(data, http.HTTP_OK)


class NonCompliantCompanyList(Resource):
    def get(self):
        limit = request.args.get(ApiConfig.LIMIT, default=0, type=int)
        offset = request.args.get(ApiConfig.OFFSET, default=0, type=int)

        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.NONCOMPLIANT,
                                                                     limit=limit, offset=offset)

        result, success = get_query.get_company_number(CompliantConfig.NONCOMPLIANT)
        count = 0

        if len(result.get(ApiConfig.DATA)):
            count = result.get(ApiConfig.DATA)[0].get(ApiConfig.COUNT)
            data[ApiConfig.TOTAL_ITEM] = count

        if len(data.get(ApiConfig.DATA)) and limit:
            length = len(data.get(ApiConfig.DATA))
            next_offset = length + offset
            if count <=next_offset:
                next_offset = 0
            data[ApiConfig.NEXT_OFFSET] = next_offset

        return make_response(data, http.HTTP_OK)


class NonCompliantCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.NONCOMPLIANT,
                                                                     symbol=id)
        return make_response(data, http.HTTP_OK)


class YellowCompanyList(Resource):
    def get(self):
        limit = request.args.get(ApiConfig.LIMIT, default=0, type=int)
        offset = request.args.get(ApiConfig.OFFSET, default=0, type=int)

        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.YELLOW,
                                                                     limit=limit, offset=offset)

        result, success = get_query.get_company_number(CompliantConfig.YELLOW)
        count = 0

        if len(result.get(ApiConfig.DATA)):
            count = result.get(ApiConfig.DATA)[0].get(ApiConfig.COUNT)
            data[ApiConfig.TOTAL_ITEM] = count

        if len(data.get(ApiConfig.DATA)) and limit:
            length = len(data.get(ApiConfig.DATA))
            next_offset = length + offset
            if count <=next_offset:
                next_offset = 0
            data[ApiConfig.NEXT_OFFSET] = next_offset

        return make_response(data, http.HTTP_OK)


class YellowCompany(Resource):
    def get(self, id):
        data, success = get_query.get_compliant_type_company_details(compliant_type=CompliantConfig.YELLOW,
                                                                     symbol=id)
        return make_response(data, http.HTTP_OK)


class CompanySearch(Resource):
    def get(self, id):
        data, success = get_query.company_search(id)
        return make_response(data, http.HTTP_OK)
