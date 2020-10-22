from src.message import password
from src.mail.mailing import send_mail
from src.config import MAILConfig


def forget_password_message(reciver, user_name, verification_code):
    mail_body, mail_header = password.verify_code_msg(user_name, verification_code)
    mail_sender = MAILConfig.SENDER
    send_mail(mail_body, mail_sender, reciver, mail_header)


def send_password_change_message(reciver, user_name):
    mail_body, mail_header = password.new_password_msg(user_name)
    mail_sender = MAILConfig.SENDER
    send_mail(mail_body, mail_sender, reciver, mail_header)
