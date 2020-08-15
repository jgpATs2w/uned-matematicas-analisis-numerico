from __future__ import division
from sympy import *

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
integrate(exp(-x), (x, 0, oo))
#expr = Integral(log(x)**2, x)