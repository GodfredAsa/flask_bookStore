from flask_restful import reqparse
from constants.user_constants import *
from models.user_model import UserModel
from typing import Tuple
import bcrypt
_user_parser = reqparse.RequestParser()
_user_parser.add_argument("firstName", type=str, required=True, help=BLANK_ERROR.format("firstName"))
_user_parser.add_argument("lastName", type=str, required=True, help=BLANK_ERROR.format("lastName"))
_user_parser.add_argument("email", type=str, required=True, help=BLANK_ERROR.format("email"))
_user_parser.add_argument("imageUrl", type=str, required=True, help=BLANK_ERROR.format("imageUrl"))
_user_parser.add_argument("username", type=str, required=True, help=BLANK_ERROR.format("username"))
_user_parser.add_argument("password", type=str, required=True, help=BLANK_ERROR.format("password"))
_user_parser.add_argument("wallet", type=str,  help=BLANK_ERROR.format("wallet"))


def user_data():
    return _user_parser.parse_args()


def validate_users(postedDate):
    user = postedDate["userEmail"]
    adminEmail = postedDate["adminEmail"]
    return UserModel.find_by_email(adminEmail), UserModel.find_by_email(user)


def user_exist(username):
    if not UserModel.find_by_email(username):
        return False
    else:
        return True


def generate_return_dictionary(status, message):
    retJson = {"status": status, "message": message}
    return retJson


def verify_credentials(username, password):
    if not user_exist(username):
        return generate_return_dictionary(301, "invalid username"), True

    def verify_password(email, password):
        if not UserModel.find_by_email(email):
            return False
        hashed_password = UserModel.find_by_email(email).password
        if bcrypt.hashpw(password.encode('utf8'), hashed_password) == hashed_password:
            return True
        else:
            return False

    correct_password = verify_password(username, password)
    if not correct_password:
        return generate_return_dictionary(302, "invalid password"), True

    # means no error
    return None, False





