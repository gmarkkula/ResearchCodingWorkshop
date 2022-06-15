import numpy as np
import matplotlib.pyplot as plt

# constants
N_GROUPS = 3
GROUP_DATA_FILE_FORMAT = 'grpdata%i.csv'
VALID_DATA_COLUMN = 1

# function for loading the data for one group
def load_group_data(i_group):
    # read from CSV file
    file_name = GROUP_DATA_FILE_FORMAT % i_group
    all_group_data = np.loadtxt(file_name, delimiter=',')
    # make sure all values in the first column are zero
    assert(np.all(all_group_data[:, 0] == 0))
    # get and return only the valid part of the data
    group_data = all_group_data[:, VALID_DATA_COLUMN]
    return group_data


# loop through groups, load data and get mean for each
group_means = np.full(N_GROUPS, np.nan)
for i_group in range(N_GROUPS):
    group_data = load_group_data(i_group)
    group_means[i_group] = np.mean(group_data)

# print the mean values
print(group_means)

# plot the means
plt.plot(group_means)
plt.xlabel('Group')
plt.ylabel('Mean value')
plt.show()