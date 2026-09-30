import unittest
import sqlite3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.routes.account import get_account_by_id

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        c = self.conn.cursor()
        c.execute('CREATE TABLE accounts (id INTEGER, owner TEXT)')
        c.execute("INSERT INTO accounts VALUES (1, 'alice')")
        self.conn.commit()

    def test_lookup(self):
        row = get_account_by_id(self.conn, 1)
        self.assertEqual(row[1], 'alice')

if __name__ == '__main__':
    unittest.main()
