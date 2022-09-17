import unittest
import category_model


class TestItem(unittest.TestCase):
    def setUp(self) -> None:
        self._Category = category_model.Category(category_id=1, item_name="fastfood", meal="lunch")

    def test_init(self):
        self.assertEqual(self._Category.category_id, 1)
        self.assertEqual(self._Category.category_name, "fastfood")
        self.assertEqual(self._Category.meal, "lunch")


if __name__ == '__main__':
    unittest.main()
