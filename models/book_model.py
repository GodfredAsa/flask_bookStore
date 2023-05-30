from db import db
from typing import List
from utils.utils import format_created_date, generate_uuid


class BookModel(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(20))
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)
    imageUrl = db.Column(db.String(200))
    createdAt = db.Column(db.String(10))

    def __init__(self, title, author, description, price, qty, imageUrl):
        self.title = title
        self.author = author
        self.description = description
        self.price = price
        self.qty = qty
        self.book_id = generate_uuid()
        self.imageUrl = imageUrl
        self.createdAt = format_created_date()

    def __str__(self):
        return f"<Book: ID:{self.id}, Title:{self.title}, Qty:{self.qty}, cost:{self.price} createdAt: {self.createdAt}>"

    def json(self):
        return {
            "bookId": self.book_id,
            "title": self.title,
            "author": self.author,
            "desc": self.description,
            "imageUrl": self.imageUrl,
            "quantity": self.qty,
            "price": self.price,
            "createdAt": self.createdAt
        }

    @classmethod
    def find_books_author(cls, author: str) -> List['BookModel']:
        return cls.query.filter_by(author=author)

    @classmethod
    def find_by_title(cls, title: str) -> 'BookModel':
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_book_id(cls, _id: str) -> List['BookModel']:
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_book_uuid(cls, book_id: str) -> List['BookModel']:
        return cls.query.filter_by(book_id=book_id).first()

    @classmethod
    def find_all_books(cls) -> List['BookModel']:
        return cls.query.all()

    def save_book_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_book_db(self) -> None:
        db.session.delete(self)
        db.session.commit()



