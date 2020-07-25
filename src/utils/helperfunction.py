import time
from datetime import datetime
from passlib.apps import custom_app_context


def hash_password(password):
    password_hash = custom_app_context.encrypt(password)
    return password_hash


def verify_password(password, hass_password):
    return custom_app_context.verify(password, hass_password)


def get_current_time_milisecond():
    return int(round(time.time() * 1000))


def get_current_time_milisecond_str():
    return str(get_current_time_milisecond())


def get_current_date():
    return datetime.today().strftime('%Y-%m-%d')


def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def get_current_date_and_time():
    return datetime.now()