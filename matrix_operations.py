import numpy as np
from sympy import Matrix, init_printing
init_printing(use_unicode=True)

A = np.array([[1,2,3,4],[5,6,7,8]])

print("first column vector:")
print(A[:,0])

M = Matrix([[1, 2, 3], [-2, 0, 4], [1,1,1]])
N = Matrix([0,1,-1])
print(M.shape)
print(M.det())
print(M**-1)
print(M*N)