import unittest
from sympy import symbols, Matrix
from io import StringIO
import sys

from test003 import A, B

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
<<<<<<< Tabnine <<<<<<<
import unittest#+
from sympy import symbols, Matrix#+
#+
class TestMatrixOperations(unittest.TestCase):#+
    def setUp(self):#+
        self.a, self.b, self.c = symbols("a b c")#+
        self.A = Matrix([[self.a, self.b], [self.c, self.a]])#+
        self.B = self.A.inv()#+
#+
if __name__ == '__main__':#+
    unittest.main()#+
>>>>>>> Tabnine >>>>>>># {"conversationId":"c88b3ec6-d3b6-4e89-9e54-82e027a88f04","source":"instruct"}
        self.a, self.b, self.c = symbols("a b c")
        self.A = Matrix([[self.a, self.b], [self.c, self.a]])
        self.B = self.A.inv()

if __name__ == '__main__':
    unittest.main()
