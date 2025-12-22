import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
x3 = np.array([0, 1, 2, 3])
y3 = np.array([1, 4, 7, 11])

plt.plot(x1, y1, x2, y2, x3, y3)
plt.show()