import unittest
import simplex

class TestSimplex(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simplex.add(1, 2), 3)
        self.assertEqual(simplex.add(-1, 2), 1)
        self.assertEqual(simplex.add(-1, -2), -3)

if __name__ == '__main__':
    unittest.main()