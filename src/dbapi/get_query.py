from src.dbconn import query, dbname, dbclass
from src.config import ApiConfig, UserConfig

def get_user_by_id(id):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE,
                                     field_name=ApiConfig.ID,
                                     offset=id)
    return result, success


def get_user_by_email(email):
    result, success = query.get_record(table_name=dbname.DBClassName.USER_TABLE,
                                     field_name=UserConfig.EMAIL,
                                     offset=email)
    return result, success