from flask_jwt_extended import jwt_required
from flask_restful import Resource
from models.sales import SaleModel
from models.book_model import BookModel
from models.user_model import UserModel
from utils.sales_utility import get_sales_parser
from constants.book_constants import *
from constants.user_constants import *


class Sale(Resource):
    @classmethod
    @jwt_required
    def post(cls):

        data = get_sales_parser()
        sale = SaleModel(**data)
        try:
            user = UserModel.find_by_email(sale.email)
            book = BookModel.find_book_uuid(sale.book_id)
            sale.total_cost = sale.qty * book.price
            if book.qty < 1:
                return {"message": BOOK_OUT_OF_STOCK.format(book.title)}
            if not user:
                return {"message": USER_NOT_FOUND}
            if user.wallet <= sale.total_cost + 1:
                return {"message": INADEQUATE_BALANCE.format(user.email)}, 404

            user.wallet = user.wallet - sale.total_cost
            sale.price = book.price
            user.save_to_db()
            book.qty = book.qty - sale.qty
            book.save_book_db()
            sale.user_id = user.user_id
            sale.save_to_db()
            return sale.json()

        except AttributeError as e:
            print("An Attribute Error Occurred", str(e))
            return {"message": BOOK_SALE_ERROR}

    @classmethod
    @jwt_required
    def get(cls):
        return [b.json() for b in SaleModel.query.all()]
