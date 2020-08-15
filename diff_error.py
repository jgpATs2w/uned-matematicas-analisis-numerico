import numpy as np

x = 1.0;
h = np.array([1e-15, 1e-14, 1e-10]);
print(((x+h)-x)/h - 1.0)
x1= x + h
dx= x1 - x
print(dx/h-1.0)