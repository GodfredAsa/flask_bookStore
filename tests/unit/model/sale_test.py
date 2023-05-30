from models.sales import SaleModel
from models.book_model import BookModel
from tests.unit.unit_base_test import UnitBaseTest


class SaleTest(UnitBaseTest):

    def test_create_sale(self) -> None:
        book = BookModel("Ananse", "Anansewa", "desc", 3.0, 2, "book.jpeg")
        sale = SaleModel(2, "user@user.com", book_id=book.book_id)
        self.assertEqual(book.book_id, sale.book_id)
        self.assertEqual(sale.qty, 2)
        self.assertEqual(sale.price, None)
        self.assertEqual(sale.id, None)
        self.assertIsNotNone(sale.sale_id)
