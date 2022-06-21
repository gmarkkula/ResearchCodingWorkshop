import numpy as np
import matplotlib.pyplot as plt

ym = np.full(3, np.nan)

ym[0] = np.mean(np.loadtxt('grpdata0.csv', delimiter=',')[:, 1])
ym[1] = np.mean(np.loadtxt('grpdata1.csv', delimiter=',')[:, 1])
ym[2] = np.mean(np.loadtxt('grpdata2.csv', delimiter=',')[:, 1])

plt.plot(ym)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()