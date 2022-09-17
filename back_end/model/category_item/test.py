import unittest
from category_item_model import category_item


class category_item_test(unittest.TestCase):
    def setUp(self) -> None:
        self._category_item = category_item(category_id=category, menu_item_id=menu_item)

    def test_init(self):
        self.assertEqual(self._category_item.user_id, category)
        self.assertEqual(self._category_item.item_id, menu_item)

        # self.assertEqual(self._order.save_orders(), 'ok')


if __name__ == '__main__':
    unittest.main()
