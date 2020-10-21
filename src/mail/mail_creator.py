from src.message import password
from src.mail.mailing import send_mail
from src.config import MAILConfig


def send_password_change_message(reciver, new_password, old_password=None):
    mail_body, mail_header = password.new_password_msg(new_password, old_password)
    mail_sender = MAILConfig.SENDER
    send_mail(mail_body, mail_sender, reciver, mail_header)
