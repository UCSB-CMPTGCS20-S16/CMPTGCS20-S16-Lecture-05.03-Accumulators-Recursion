import unittest

class TestMySum(unittest.TestCase):

    def test_mySum_a(self):
        self.assertEqual(mySum([]), 0)

    def test_mySum_b(self):
        self.assertEqual(mySum([7]), 7)

    def test_mySum_c(self):
        self.assertEqual(mySum([7, 3]), 10)

    def test_mySum_c(self):
        self.assertEqual(mySum([7, 3, 1, 2, 3]), 16)


if __name__=="__main__":
    unittest.main()
    
