from flask_restful import Resource
from constants.book_constants import *
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required, get_raw_jwt, jwt_refresh_token_required,
)
from blacklist import BLACKLIST
from models.book_model import BookModel
from utils.book_utils import book_data


class CreateBook(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        data = book_data()
        if BookModel.find_by_title(data["title"]):
            return {"message": BOOK_ALREADY_EXISTS}, 400
        book = BookModel(**data)
        book.save_book_db()
        return book.json(), 201


class Books(Resource):
    @classmethod
    def get(cls):
        books = BookModel.find_all_books()
        return [book.json() for book in books]


# TODO currently not wotking
class Book(Resource):
    @classmethod
    @jwt_required
    def get(cls, title):
        book = BookModel.find_by_title(title)
        if not book:
            return {"message": BOOK_NOT_FOUND}, 404
        return book.json()

    @classmethod
    @jwt_required
    def put(cls, title):
        book = BookModel.find_by_title(title)
        if not book:
            return {"message": BOOK_NOT_FOUND}, 404
        data = book_data()
        cls.__update_book__(book, data)
        return book.json(), 200

    @classmethod
    @jwt_required
    def delete(cls, title):
        book = BookModel.find_by_title(title)
        if not book:
            return {"message": BOOK_NOT_FOUND}, 404
        book.delete_book_db()
        return {"message": f"Book with {title} successfully deleted"}, 204

    @classmethod
    def __update_book__(cls, book, data):
        update_bok = BookModel(**data)
        book.title = update_bok.title
        book.author = update_bok.author
        book.description = update_bok.description
        book.qty = update_bok.qty
        book.price = update_bok.price
        book.save_book_db()