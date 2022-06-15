import numpy as np
import matplotlib.pyplot as plt

N_GROUPS = 3
GROUP_DATA_FILE_FORMAT = 'grpdata%i.csv'
VALID_DATA_COLUMN = 1

group_means = np.full(N_GROUPS, np.nan)
for i_group in range(N_GROUPS):
    file_name = GROUP_DATA_FILE_FORMAT % i_group
    all_group_data = np.loadtxt(file_name, delimiter=',')
    group_data = all_group_data[:, VALID_DATA_COLUMN]
    group_means[i_group] = np.mean(group_data)

plt.plot(group_means)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()