import unittest
from table_model import tables

class table_test(unittest.TestCase):
    def setUp(self) -> None:
        self._table = tables(table_number=8,capacity=6,booking=True)

    def test_init(self):
        self.assertEqual(self._table.table_number,8)
        self.assertEqual(self._table.capacity,6)
        self.assertEqual(self._table.booking,True)
        
if __name__ == '__main__':
    unittest.main()
