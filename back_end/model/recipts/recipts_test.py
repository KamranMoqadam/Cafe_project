from distutils.command.install_egg_info import to_filename
import unittest
from recipts_model import receipts

class receipt_test(unittest.TestCase):
    def setUp(self) -> None:
        self._receipt = receipts(order_id=1, user_id=1, total_price='20$')
        
    def test_init(self):
        self.assertEqual(self._receipt.order_id, 1)
        self.assertEqual(self._receipt.user_id, 1)
        self.assertEqual(self._receipt.total_price, '20$')
        self.assertEqual(self._receipt.final_price, '20$')
        
        
if __name__ == '__main__':
    unittest.main()
       