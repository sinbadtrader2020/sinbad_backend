import json

from src.dbapi import get_query, update_query
from src.dbconn.dbclass.user import User
from src.config import UserConfig, ApiConfig
from src.utils.defaultclass import Struct
from src.utils import pmemcached, pro_time
from src.http import http
from src.utils.random_string import get_verification_code
from src.mail.mail_creator import send_password_change_message, forget_password_message


def reset_password(data):
    email = data[UserConfig.EMAIL]
    user_details, sucess = get_query.get_user_by_email(email)

    if len(user_details.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'User is Not Exist', http.HTTP_NOT_FOUND

    verification_code = get_verification_code()

    user_details_obj = Struct(**user_details.get(ApiConfig.DATA)[0])
    pmemcached.setvalue(key=verification_code, value=email, time=pro_time.min_to_second(min=10))
    forget_password_message(email, user_details_obj.first_name, verification_code)

    return 'User verification code send to mail', http.HTTP_ACCEPTED


def change_password(data):
    email = data[UserConfig.EMAIL]
    password = data[UserConfig.PASSWORD]
    new_password = data[UserConfig.NEW_PASSWORD]

    user_details, sucess = get_query.get_user_by_email(email)

    if len(user_details.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'User is Not Exist', http.HTTP_NOT_FOUND

    user_details_obj = Struct(**user_details.get(ApiConfig.DATA)[0])


    if user_details_obj.password != password:
        return 'Invalid Credentials', http.HTTP_NOT_FOUND

    user_details = User()
    user_details.password = new_password
    user_details_str = json.dumps(user_details.__dict__, sort_keys=True, indent=1)
    user_details_json = json.loads(user_details_str)

    user_update, sucess = update_query.update_user(user_details_json, user_details_obj.id)

    if len(user_update.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'Fail to Update user Data', http.HTTP_NOT_MODIFIED

    send_password_change_message(email, user_details_obj.first_name)

    return 'Successfully user password updated.', http.HTTP_ACCEPTED


def verify_user_code(data):
    verify_code = data[UserConfig.VERIFY_CODE]
    email = data[UserConfig.EMAIL]

    key_value = pmemcached.getvalue(verify_code)

    if key_value == None:
        return 'Wrong verification code.', http.HTTP_UNAUTHORIZED

    if email != key_value:
        return 'Wrong verification code.', http.HTTP_UNAUTHORIZED
    else:
        return 'Successfully match with token.', http.HTTP_ACCEPTED


def forget_change_password(data):
    email = data[UserConfig.EMAIL]
    password = data[UserConfig.PASSWORD]

    user_details, sucess = get_query.get_user_by_email(email)

    if len(user_details.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'User is Not Exist', http.HTTP_NOT_FOUND

    user_details_obj = Struct(**user_details.get(ApiConfig.DATA)[0])

    user_details = User()
    user_details.password = password
    user_details_str = json.dumps(user_details.__dict__, sort_keys=True, indent=1)
    user_details_json = json.loads(user_details_str)

    user_update, sucess = update_query.update_user(user_details_json, user_details_obj.id)

    if len(user_update.get(ApiConfig.DATA)) == 0 or sucess == False:
        return 'Fail to Update user Data', http.HTTP_NOT_MODIFIED

    send_password_change_message(email, user_details_obj.first_name)

    return 'Successfully user password updated.', http.HTTP_ACCEPTED
