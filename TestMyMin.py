import unittest

from myMin import myMin

class TestMyMin(unittest.TestCase):

    def test_myMin_a(self):
        self.assertEqual(myMin([]),False)

    def test_myMin_b(self):
        self.assertEqual(myMin([-5]),-5)

    def test_myMin_c(self):
        self.assertEqual(myMin([-5,2]),-5)

    def test_myMin_d(self):
        self.assertEqual(myMin([2,-5]),-5)

    def test_myMin_e(self):
        self.assertEqual(myMin([5,16,32,24,3]),3)
