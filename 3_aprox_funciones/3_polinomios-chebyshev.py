import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.linspace(-1, 1, 2000)
y = x ** 3 + 2 * x ** 2
p = np.polynomial.Chebyshev.fit(x, y, 2)

plt.plot(x, y, 'r.', label='original')
plt.plot(x, p(x), 'k-', lw=3, label='aproximation')
plt.legend()
plt.show()