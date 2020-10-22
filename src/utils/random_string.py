import random
import string


def generate_random_password():
    return get_random_string(10)


def get_verification_code(len=6):
    return get_random_string(len)


def get_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    print("Random string of length", length, "is:", result_str)
    return result_str