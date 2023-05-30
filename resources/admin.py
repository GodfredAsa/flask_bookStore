from flask_restful import Resource
from flask import request
from utils.user_utils import validate_users
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required, get_raw_jwt, jwt_refresh_token_required,
)


class Admin(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        try:
            postedDate = request.get_json()
            admin, user = validate_users(postedDate)
            if admin.is_admin:
                user.is_admin = True
                user.save_to_db()
                return user.json(), 200
            return {"message": "You are not authorised to access this resource"}, 401
        except AttributeError as e:
            print("Invalid Email", str(e))

    @classmethod
    @jwt_required
    def put(cls):
        postedDate = request.get_json()
        transfer = postedDate["transferAmount"]
        try:
            admin, user = validate_users(postedDate)
            if admin.is_admin:
                user.wallet += transfer
                user.save_to_db()
                return user.json(), 200
            return {"message": "You are not authorised to access this resource"}, 401
        except AttributeError as e:
            print("check email entered \n" + str(e))
            return {"message": "Error Occurred" }, 400
            # print("Invalid Email Entry", str(e))
