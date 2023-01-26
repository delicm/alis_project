import numpy as np
from matplotlib import pyplot as plt

n=100
plt.scatter([i for i in range(n)], np.random.permutation([i for i in range(n)]))
plt.show()
