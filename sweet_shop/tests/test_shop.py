import unittest

class TestSetup(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(100 + 20, 120)

if __name__ == "__main__":
    unittest.main()
