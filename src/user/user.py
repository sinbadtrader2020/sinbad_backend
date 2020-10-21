import json

from src.dbapi import get_query, update_query
from src.dbconn.dbclass.user import User
from src.config import UserConfig, ApiConfig
from src.utils.defaultclass import Struct
from src.http import http
from src.utils.random_string import generate_random_password
from src.mail.mail_creator import send_password_change_message


def reset_password(data):
    print(data[UserConfig.EMAIL])
    user_details, sucess = get_query.get_user_by_email(data[UserConfig.EMAIL])

    if len(user_details.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'User is Not Exist', http.HTTP_NOT_FOUND

    user_details_obj = Struct(**user_details.get(ApiConfig.DATA)[0])
    user_details = User()
    user_details.password = generate_random_password()
    new_password = user_details.password
    user_details_str = json.dumps(user_details.__dict__, sort_keys=True, indent=1)
    user_details_json = json.loads(user_details_str)

    user_update, sucess = update_query.update_user(user_details_json, user_details_obj.id)

    if len(user_update.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'Fail to Update user Data', http.HTTP_NOT_MODIFIED

    send_password_change_message(data[UserConfig.EMAIL], new_password)

    return 'Successfully user password Update', http.HTTP_ACCEPTED


def change_password(data):
    email = data[UserConfig.EMAIL]
    password = data[UserConfig.PASSWORD]
    new_password = data[UserConfig.NEW_PASSWORD]

    user_details, sucess = get_query.get_user_by_email(email)

    if len(user_details.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'User is Not Exist', http.HTTP_NOT_FOUND

    user_details_obj = Struct(**user_details.get(ApiConfig.DATA)[0])


    if user_details_obj.password != password:
        return 'Password is Not Verified', http.HTTP_NOT_FOUND

    user_details = User()
    user_details.password = new_password
    user_details_str = json.dumps(user_details.__dict__, sort_keys=True, indent=1)
    user_details_json = json.loads(user_details_str)

    user_update, sucess = update_query.update_user(user_details_json, user_details_obj.id)

    if len(user_update.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'Fail to Update user Data', http.HTTP_NOT_MODIFIED

    send_password_change_message(email, new_password, old_password=password)

    return 'Successfully user password Update', http.HTTP_ACCEPTED
