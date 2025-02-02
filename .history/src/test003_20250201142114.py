from sympy import symbols, Matrix
import pprint


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
    """_summary_
    """)   



