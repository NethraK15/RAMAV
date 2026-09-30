import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.services.order import apply_discount

class TestOrderRegression(unittest.TestCase):
    def test_member_discount_is_ten_percent(self):
        self.assertEqual(apply_discount(100.0, True), 90.0)

if __name__ == '__main__':
    unittest.main()
