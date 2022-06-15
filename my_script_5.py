import numpy as np
import matplotlib.pyplot as plt

ym = np.full(3, np.nan)

ayd = np.loadtxt('grpdata0.csv', delimiter=',')
yd = ayd[:, 1]
ym[0] = np.mean(yd)

ayd = np.loadtxt('grpdata1.csv', delimiter=',')
yd = ayd[:, 1]
ym[1] = np.mean(yd)

ayd = np.loadtxt('grpdata2.csv', delimiter=',')
yd = ayd[:, 1]
ym[2] = np.mean(yd)

plt.plot(ym)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()