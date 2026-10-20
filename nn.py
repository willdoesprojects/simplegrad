import numpy as np

x = np.array([1, 2, 3])
w = np.array([0.4, 0.5, -0.2])
b = 0.1

value = np.dot(x,w) + b
print(value)
