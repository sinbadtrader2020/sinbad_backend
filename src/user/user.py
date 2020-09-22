from src.dbapi import get_query

def get_user_infomation(id):
    user_details, sucess = get_query.get_user_by_id(id)
    return user_details, sucess
