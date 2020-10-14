from flask_mail import Mail,  Message

mail_config = None


def set_config(app):
    mail = Mail(app)
    global mail_config
    mail_config = mail


def send_mail(message, sender, recipients, Header):
    if mail_config == None:
        return 'Fail to send'
    msg = mail_config.send_message(
        Header,
        sender=sender,
        recipients=[recipients],
        body=message
    )

    return 'Mail sent'
