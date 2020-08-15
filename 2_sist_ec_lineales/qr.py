import pprint

import numpy
import scipy
import scipy.linalg

A = scipy.array([[1,1,0], [0,0,1], [0,1,1]])
Q, R = scipy.linalg.qr(A)

print("A:")
pprint.pprint(A)
print(numpy.linalg.eig(A))

print("Q:")
pprint.pprint(Q)

print("R:")
pprint.pprint(R)
print(numpy.linalg.eig(R))

