import bcrypt as bcrypt
from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required
)
from models.user_model import UserModel
from blacklist import BLACKLIST
from constants.user_constants import *
from utils.user_utils import user_data, verify_credentials
from utils.utils import generate_uuid


class RegisterUser(Resource):
    @classmethod
    def post(cls):
        data = user_data()
        if UserModel.find_by_email(data['email']):
            return {"message": USER_ALREADY_EXISTS}, 400
        user = UserModel(**data)
        user.password = bcrypt.hashpw(user.password.encode("utf8"), bcrypt.gensalt())
        user.user_id = generate_uuid()
        user.save_to_db()
        return user.json(), 201


class User(Resource):
    @classmethod
    @jwt_required
    def get(cls, email):
        user = UserModel.find_by_email(email)
        if not user:
            return {"message": USER_NOT_FOUND}, 404
        return user.json(), 200

    @classmethod
    @jwt_required
    def put(cls, email):
        user = UserModel.find_by_email(email)
        if not user:
            return {"message": USER_NOT_FOUND}, 404
        data = user_data()
        update_user = UserModel(**data)
        cls.__update_user_details__(update_user, user)
        return user.json(), 200

    @classmethod
    def __update_user_details__(cls, update_user, user):
        user.first_name = update_user.first_name
        user.last_name = update_user.last_name
        user.email = update_user.email
        user.imageUrl = update_user.imageUrl
        user.username = update_user.username
        user.save_to_db()


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()

        retJson, error = verify_credentials(data['email'], data['password'])
        if error:
            return jsonify(retJson)

        user = UserModel.find_by_email(data["email"])

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)
        return {"access_token": access_token, 'refresh_token': refresh_token}, 200


class Users(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        return [user.json() for user in UserModel.query.all()]



