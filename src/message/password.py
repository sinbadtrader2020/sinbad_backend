def verify_code_msg(username, verifycode):
    message = "Dear " + username + ",\n\n"
    message = message + "We’ve received your forget password request. This is a really simple process." \
                        ", here we need to verify your account:\n"
    message = message + "Verify Code: " + verifycode + "\n\n\n"
    message = message + "Thanks, Sinbad Finance Team" + "\n"
    header = "Your Sinbad ID verification code"
    return message, header


def new_password_msg(username):
    message = "Dear " + username + ",\n\n"
    message = message + "We’ve received your password change request. This is a really simple process.\n"
    message = message + "Recently your Sinbad Finance password has changed.\n\n\n"
    message = message + "Thanks, Sinbad Finance Team" + "\n"
    header = "Your Sinbad ID password has changed"
    return message, header
