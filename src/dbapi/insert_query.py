from src.dbconn import query, dbname, dbclass
from src.config import ApiConfig

def insert_user(data):
    result, success = query.create_record(table_name=dbname.DBClassName.USER_TABLE,
                                          field_name=ApiConfig.ID,
                                          record=dbclass.User(**data))
    return result, success