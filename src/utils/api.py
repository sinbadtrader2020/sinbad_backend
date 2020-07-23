from flask_restful import Resource, request
from src.config import ApiConfig
from src.dbconn import query
from src.http.http import get_response, GET, PUT, POST


class SimpleApi(Resource):
    def __init__(self, **kwargs):
        self.get_table = None
        self.get_field = None

        self.put_table = None
        self.put_field = None
        self.put_record = None

    def get(self, id):
        print('SimpleApi')
        result, success = query.get_record(table_name=self.get_table,
                                     field_name=self.get_field,
                                     offset=id)
        return get_response(result, success, GET)

    def put(self, id):
        print('SimpleApi')
        result, success = query.update_record(table_name=self.put_table,
                                        field_name=self.put_field,
                                        field_value=id,
                                        record=self.put_record(**request.json))
        return get_response(result, success, PUT)


class SimpleListApi(Resource):
    def __init__(self, **kwargs):
        self.get_table = None

        self.post_table = None
        self.post_field = None
        self.post_record = None

    def get(self):
        result, success = query.get_record(table_name=self.get_table,
                                     group=True,
                                     offset=0,
                                     limit=ApiConfig.DEFAULT_GET_VALUE)
        return get_response(result, success, GET)

    def post(self):
        result, success = query.create_record(table_name=self.post_table,
                                        field_name=self.post_field,
                                        record=self.post_record(**request.json))
        return get_response(result, success, POST)
