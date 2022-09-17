import unittest
from oredr_model import orders


class order_test(unittest.TestCase):
    def setUp(self) -> None:
        self._order = orders(user_id=1, table_id=1, item_id=1, number=33, status='cooking', takaway=True)

    def test_init(self):
        self.assertEqual(self._order.user_id, 1)
        self.assertEqual(self._order.item_id, 1)
        self.assertEqual(self._order.table_id, 1)
        self.assertEqual(self._order.number, 33)
        self.assertEqual(self._order.status, 'cooking')
        self.assertEqual(self._order.takeaway, True)
        # self.assertEqual(self._order.save_orders(), 'ok')


if __name__ == '__main__':
    unittest.main()
