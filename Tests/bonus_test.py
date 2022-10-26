import unittest
from bonus import calculator

def test_bonus(self):
    self.assertEqual(100, calculator(5, 100))
    self.assertEqual(105, calculator(8, 100))
    self.assertEqual(210, calculator(6, 200))

if __name__ == "__main__":
    unittest.main()