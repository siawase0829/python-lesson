from sympy import symbols, Matrix
import pprint 


a, b, c = symbols('a b c')
A = Matrix([[a, b], [c, a]])
B = A.inv()  # 
pprint.pprint(A)
aaaaaaaaaaa
pprint.pprint(B)