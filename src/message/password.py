
def new_password_msg(password, old_password=None):
    message = "Dear Customer,\n\n"
    message = message + "Recently your Sinbad Finance password has changed.\n"
    message = message + "New Password: " + password + "\n\n"
    if old_password != None:
        message = message + "Old Password: " + old_password + "\n\n"
    message = message + "Thanks, Sinbad Finance Team" + "\n"
    header = "Your Sinbad ID password has changed"
    return message, header
