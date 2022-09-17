import unittest
import item_model


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self._Item = item_model.Item(menu_id=1, item_name="pizza", price=1, category="lunch", discount=0,
                                     serving_time=None, cooking_time=None,category_id=1)

    def test_init(self):
        self.assertEqual(self._Item.menu_id, 1)
        self.assertEqual(self._Item.item_name, "pizza")
        self.assertEqual(self._Item.price, "10000")
        self.assertEqual(self._Item.category, "lunch")
        self.assertEqual(self._Item.discount, 0)
        self.assertEqual(self._Item.category_id, 1)


if __name__ == '__main__':
    unittest.main()
