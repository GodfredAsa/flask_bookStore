from flask_restful import reqparse
from constants.book_constants import *
_book_parser = reqparse.RequestParser()
_book_parser.add_argument("title", type=str, required=True, help=BLANK_ERROR.format("title"))
_book_parser.add_argument("description", type=str, required=True, help=BLANK_ERROR.format("description"))
_book_parser.add_argument("author", type=str, required=True, help=BLANK_ERROR.format("author"))
_book_parser.add_argument("imageUrl", type=str, required=True, help=BLANK_ERROR.format("imageUrl"))
_book_parser.add_argument("price", type=str, required=True, help=BLANK_ERROR.format("price"))
_book_parser.add_argument("qty", type=str, required=True, help=BLANK_ERROR.format("password"))


def book_data():
    return _book_parser.parse_args()
