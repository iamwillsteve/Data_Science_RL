import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-10, 11, 1)
b = np.arange(-10, 11, 1)
c = np.arange(-10, 11, 1)

x = np.linspace(-25, 25, 100)
a, b, c = np.meshgrid(a, b, c, indexing='ij')
y = -10*x**2 + -10*x + -10
plt.plot(x, y, 'ro')
print(a, b, c)