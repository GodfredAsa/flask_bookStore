from models.book_model import BookModel
from tests.unit.unit_base_test import UnitBaseTest
from utils.utils import format_created_date


class BookTest(UnitBaseTest):

    def test_create_book(self):
        book = BookModel("Ananse", "Anansewa", "desc", 3.0, 2, "book.jpeg")
        self.assertEqual(book.title, "Ananse", "book title")
        self.assertEqual(book.author, "Anansewa", "book author")
        self.assertEqual(book.description, "desc", "book description")
        self.assertEqual(book.price, 3.0, "book price")
        self.assertEqual(book.qty, 2, "book qty")

    def test_book_json(self):
        book = BookModel("Ananse", "Anansewa", "desc", 3.0, 2, "book.jpeg")
        book.book_id = "1234"

        expected_json = {"bookId": "1234", "title": "Ananse", "author": "Anansewa", "desc": "desc",
                         "imageUrl": "book.jpeg", "quantity": 2, "price": 3.0, "createdAt": format_created_date()
                         }

        actual_json = book.json()

        self.assertDictEqual(expected_json, actual_json)




