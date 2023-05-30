from typing import Union, Any

from flask_restful import reqparse
from constants.sales_constant import *
from models.book_model import BookModel

_sales_parser = reqparse.RequestParser()
_sales_parser.add_argument("email", type=str, required=True, help=BLANK_ERROR.format("email"))
_sales_parser.add_argument("book_id", type=str, required=True, help=BLANK_ERROR.format("book"))
_sales_parser.add_argument("qty", type=str, required=True, help=BLANK_ERROR.format("qty"))


def get_sales_parser():
    return _sales_parser.parse_args()


def calculate_cost(title: str, qty: int) -> float:
    return validate_book(title).price * float(qty)


def get_book_price(title: str) -> Union[str, float]:
    return validate_book(title).price


def validate_book(title: str) -> Union[Any, "BookModel"]:
    book = BookModel.find_by_title(title)
    if not book:
        return "Book Not Found"
    return book
