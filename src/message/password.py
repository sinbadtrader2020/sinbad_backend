def verify_code_msg(username, verifycode):
    message = "Dear " + username + ",\n\n"
    message = message + "We’ve received your forget password request. This is a really simple process." \
                        " We need to verify your account first.\n"
    message = message + "Use this verification Code: " + verifycode + "\n\n\n"
    message = message + "Thanks, \n"
    message = message + "Sinbad Finance Team\n"
    header = "Reset your SINBAD password"
    return message, header


def new_password_msg(username):
    message = "Dear " + username + ",\n\n"
    message = message + "Your Sinbad Finance password has been changed recently.\n\n\n"
    message = message + "Thanks," + "\n"
    message = message + "Sinbad Finance Team" + "\n"
    header = "Changed your SINBAD password"
    return message, header
