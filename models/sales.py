from db import db
from typing import List
from models.book_model import BookModel
from utils.sales_utility import calculate_cost, get_book_price
from utils.utils import generate_uuid


class SaleModel(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.String(20))
    user_id = db.Column(db.String(100), db.ForeignKey("users.id"))
    email = db.Column(db.String(80))
    qty = db.Column(db.Integer)
    price = db.Column(db.Float(precision=2))
    total_cost = db.Column(db.Float(precision=2))

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    book = db.relationship("BookModel")

    def __init__(self, qty, email, book_id):
        self.sale_id = generate_uuid()
        self.book_id = book_id
        self.email = email
        self.total_cost = 0.0
        self.qty = int(qty)

    def __str__(self):
        return f"<Sale: ID:{self.id}, Book:{self.book}, Qty:{self.qty} price:{self.price} cost:{self.total_cost}>"

    def json(self):
        return {
            "saleId": self.sale_id,
            "user": self.email,
            "qty": self.qty,
            "bookId": self.book_id,
            "price": self.price,
            "totalCost": self.total_cost
        }

    @classmethod
    def find_all_sales(cls) -> List['SaleModel']:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
