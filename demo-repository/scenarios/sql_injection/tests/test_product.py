import unittest
import sqlite3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.routes.product import get_product_by_sku

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        c = self.conn.cursor()
        c.execute('CREATE TABLE products (id INTEGER, name TEXT, price REAL, sku TEXT)')
        c.execute("INSERT INTO products VALUES (1, 'Widget', 9.99, 'SKU1')")
        self.conn.commit()

    def test_lookup(self):
        row = get_product_by_sku(self.conn, 'SKU1')
        self.assertEqual(row[1], 'Widget')

if __name__ == '__main__':
    unittest.main()
