import unittest
from users_model import Users

"""
Applying Users attributes test
"""


class UsersTest(unittest.TestCase):
    def setUp(self) -> None:
        self._user = Users(first_name="ADIB", last_name="ZANDKARIMI", phone="09123458765", email="adib@gmail.com",
                           address="Sanandaj", password="12345678", type="customer")

    def test_init(self):
        self.assertEqual(self._user.first_name, "ADIB")
        self.assertEqual(self._user.last_name, "ZANDKARIMI")
        self.assertEqual(self._user.phone, "09123458765")
        self.assertEqual(self._user.email, "adib@gmail.com")
        self.assertEqual(self._user.address, 'Sanandaj')
        self.assertEqual(self._user.password, "12345678")
        self.assertEqual(self._user.type, "customer")


if __name__ == '__main__':
    unittest.main()
