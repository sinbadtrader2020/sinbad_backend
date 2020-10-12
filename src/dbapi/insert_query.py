from src.dbconn import query
from src.dbconn.dbname import DBClassName
from src.dbconn.dbclass.user import User
from src.dbconn.dbclass.subscribe_user import SubscribeUser
from src.config import ApiConfig


def insert_user(data):
    result, success = query.create_record(table_name=DBClassName.USER_TABLE,
                                          field_name=ApiConfig.ID,
                                          record=User(**data))
    return result, success


def insert_subscribe_user(data):
    result, success = query.create_record(table_name=DBClassName.SUBSCRIBE_USER,
                               field_name=ApiConfig.ID,
                               record=SubscribeUser(**data))
    return result, success


def insert_get_app_url_user(data):
    result, success = query.create_record(table_name=DBClassName.GET_APP_URL_USER,
                               field_name=ApiConfig.ID,
                               record=SubscribeUser(**data))
    return result, success