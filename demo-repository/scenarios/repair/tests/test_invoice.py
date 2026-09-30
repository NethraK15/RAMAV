import unittest
import sqlite3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.routes.invoice import get_invoice_by_customer

class TestInvoice(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        c = self.conn.cursor()
        c.execute('CREATE TABLE invoices (id INTEGER, total REAL, customer TEXT)')
        c.execute("INSERT INTO invoices VALUES (1, 42.5, 'alice')")
        self.conn.commit()

    def test_lookup(self):
        row = get_invoice_by_customer(self.conn, 'alice')
        self.assertEqual(row[1], 42.5)

if __name__ == '__main__':
    unittest.main()
