import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 10)

plt.hist(x, 10)
plt.show()
