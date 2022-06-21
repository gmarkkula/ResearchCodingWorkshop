import numpy as np
import matplotlib.pyplot as plt

N_GROUPS = 3
VALID_DATA_COLUMN = 1

group_means = np.full(N_GROUPS, np.nan)

all_group_data = np.loadtxt('grpdata0.csv', delimiter=',')
group_data = all_group_data[:, VALID_DATA_COLUMN]
group_means[0] = np.mean(group_data)

all_group_data = np.loadtxt('grpdata1.csv', delimiter=',')
group_data = all_group_data[:, VALID_DATA_COLUMN]
group_means[1] = np.mean(group_data)

all_group_data = np.loadtxt('grpdata2.csv', delimiter=',')
group_data = all_group_data[:, VALID_DATA_COLUMN]
group_means[2] = np.mean(group_data)

plt.plot(group_means)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()