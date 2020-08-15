import sympy as sy
sy.init_printing()

a, b, c, d = sy.symbols('a b c d')
A = sy.Matrix([[a-b, b+c],[3*d + c, 2*a - 4*d]])
B = sy.Matrix([[8, 1],[7, 6]])

sy.pprint(sy.solve(A - B, (a, b, c, d)))

x1,x2, x3 = sy.symbols('x1 x2 x3')
A = sy.Matrix(3,3,[1,0,0, 0,1,0, 0,0,1])
X = sy.Matrix([1,x1,x2])
B = sy.Matrix([0,0,1])

sy.system = A,b = A, B
sy.pprint(sy.linsolve(sy.system, x1,x2))