import unittest

class TestBasicSanity(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_string_formatting(self):
        self.assertEqual(f"{'a'}{'b'}", 'ab')

if __name__ == '__main__':
    unittest.main()
