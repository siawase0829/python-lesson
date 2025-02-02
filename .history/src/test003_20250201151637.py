# This Python code snippet is using the SymPy library to perform symbolic matrix operations. Here's a
# breakdown of what the code is doing:
# `from sympy import symbols, Matrix` is importing the `symbols` and `Matrix` classes from the SymPy
# library. The `symbols` function is used to create symbolic variables, while the `Matrix` class is
# used to define matrices and perform matrix operations in a symbolic way.
from sympy import symbols, Matrix
import pprint

# Define symbols for the elements of the matrix A
# This Python code snippet is using the SymPy library to perform symbolic matrix operations. Here's a
# breakdown of what the code is doing:
a, b, c = symbols("a b c")
A = Matrix([[a, b], [c, a]])
B = A.inv()  #
pprint.pprint(A)
pprint.pprint(B)
pprint.pprint(A * B)
pprint.pprint(B * A)

pprint.pprint(A * B)
for i in map(lambda x: x**2, range(10)):
    print(i)

