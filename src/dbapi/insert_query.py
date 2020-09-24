from src.dbconn import query
from src.dbconn.dbname import DBClassName
from src.dbconn.dbclass.user import User
from src.config import ApiConfig

def insert_user(data):
    result, success = query.create_record(table_name=DBClassName.USER_TABLE,
                                          field_name=ApiConfig.ID,
                                          record=User(**data))
    return result, success