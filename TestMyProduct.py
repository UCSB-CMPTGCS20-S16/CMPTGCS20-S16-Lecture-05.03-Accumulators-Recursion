import unittest
from myProduct import myProduct

class TestMyProduct(unittest.TestCase):

    def test_myProduct_a(self):
        self.assertEqual(myProduct([]), 1)

    def test_myProduct_b(self):
        self.assertEqual(myProduct([7]), 7)

    def test_myProduct_c(self):
        self.assertEqual(myProduct([7, 3]), 21)

    def test_myProduct_d(self):
        self.assertEqual(myProduct([7, 3, 1, 2, 3]), 126)


if __name__=="__main__":
    unittest.main()
    
