from src.dbconn import query, dbname, dbclass
from src.config import ApiConfig


def update_user(data, id):
    result, success = query.update_record(table_name=dbname.DBClassName.USER_TABLE,
                                          field_name=ApiConfig.ID,
                                          field_value=id,
                                          record=dbclass.User(**data))
    return result, success