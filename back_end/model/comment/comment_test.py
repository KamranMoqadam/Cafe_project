import unittest
from comment_model import comment


class order_test(unittest.TestCase):
    def setUp(self) -> None:
        self._comment = comment(user_id=1, menu_id=1, comment_text="not good", rate=5)

    def test_init(self):
        self.assertEqual(self._comment.user_id, 1)
        self.assertEqual(self._comment.menu_id, 1)
        self.assertEqual(self._comment.comment_text, "not good")
        self.assertEqual(self._comment.rate, 5)
        # self.assertEqual(self._order.save_orders(), 'ok')


if __name__ == '__main__':
    unittest.main()
