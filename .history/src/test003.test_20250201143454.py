import unittest
from sympy import symbols, Matrix
from io import StringIO
import sys

from test003 import A, B

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
import unittest
from sympy import symbols, Matrix

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.a, self.b, self.c = symbols("a b c")
        self.A = Matrix([[self.a, self.b], [self.c, self.a]])
        self.B = self.A.inv()

if __name__ == '__main__':
    unittest.main()
    self.a, self.b, self.c = symbols("a b c")
    self.A = Matrix([[self.a, self.b], [self.c, self.a]])
    self.B = self.A.inv()

if __name__ == '__main__':
    unittest.main()
