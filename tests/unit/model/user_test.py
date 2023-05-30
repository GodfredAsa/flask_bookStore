from models.user_model import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("testA", "testB", "test", "test@test@test.com", "image.png", "pass", 2.0)
        self.assertEqual(user.first_name, "testA")
        self.assertEqual(user.wallet, 2.0)

    def test_user_json(self):
        user = UserModel("testA", "testB", "test", "test@test@test.com", "image.png", "pass", 2.0)
        expected_json = {
            "userId": None, "firstName": "testA", "lastName": "testB",
            "email": "test@test@test.com", "imageUrl": "image.png",
            "isAdmin": None, "wallet": 2.0, "username": "test"
        }

        self.assertDictEqual(expected_json, user.json())

