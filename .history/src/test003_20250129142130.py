
from sympy import symbols, Matrix


a, b, c = symbols('a b c')
A = Matrix([[a, b], [c, a]])
B = A.inv()  # 逆行列

print(B)
