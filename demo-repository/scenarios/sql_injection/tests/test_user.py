import unittest
import sqlite3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from app.routes.user import get_user_by_username

class TestUser(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        c = self.conn.cursor()
        c.execute('CREATE TABLE users (id INTEGER, username TEXT, email TEXT)')
        c.execute("INSERT INTO users VALUES (1, 'alice', 'alice@example.com')")
        self.conn.commit()

    def test_lookup_existing_user(self):
        row = get_user_by_username(self.conn, 'alice')
        self.assertEqual(row[1], 'alice')
    # This test only covers the normal/expected lookup path; it does
    # not add any adversarial or attacker-supplied-input coverage.

if __name__ == '__main__':
    unittest.main()
