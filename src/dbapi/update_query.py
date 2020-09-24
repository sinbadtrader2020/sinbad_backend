from src.dbconn import query
from src.dbconn.dbname import DBClassName
from src.dbconn.dbclass.user import User
from src.config import ApiConfig


def update_user(data, id):
    result, success = query.update_record(table_name=DBClassName.USER_TABLE,
                                          field_name=ApiConfig.ID,
                                          field_value=id,
                                          record=User(**data))
    return result, success