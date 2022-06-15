import numpy as np
import matplotlib.pyplot as plt

N_GROUPS = 3
GROUP_DATA_FILE_FORMAT = 'grpdata%i.csv'
VALID_DATA_COLUMN = 1

def load_group_data(i_group):
    file_name = GROUP_DATA_FILE_FORMAT % i_group
    all_group_data = np.loadtxt(file_name, delimiter=',')
    group_data = all_group_data[:, VALID_DATA_COLUMN]
    return group_data


group_means = np.full(N_GROUPS, np.nan)
for i_group in range(N_GROUPS):
    group_data = load_group_data(i_group)
    group_means[i_group] = np.mean(group_data)

plt.plot(group_means)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()