import numpy as np

n = 5

aij = lambda i, j: np.where(i == j,
                            np.where(i == 0,
                                     1,
                                     1 + (i+1) ** 2),
                            np.where(
                                np.logical_or(i == j + 1, j == i + 1),
                                np.where( j == i+1, -(i+1),-(j+1)),
                                0))

A = np.fromfunction(aij, (n, n), dtype=int)

print(A)

print("det: %d" % np.linalg.det(A))
L = np.linalg.cholesky(A)
print(L)