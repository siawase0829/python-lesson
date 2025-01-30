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
)   

Since there was no specific request provided, I cannot generate code to fill in the [BLANK]. Additionally, the code shown has a syntax error with an extra closing parenthesis `)` before the [BLANK]. Without a clear requirement for what functionality should be added, I cannot provide appropriate code to insert at that location.
