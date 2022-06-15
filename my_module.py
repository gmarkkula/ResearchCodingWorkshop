import numpy as np

# constants
N_GROUPS = 3
GROUP_DATA_FILE_FORMAT = 'grpdata%i.csv'
VALID_DATA_COLUMN = 1

# load the data for one group
def load_group_data(i_group):
    # read from CSV file
    file_name = GROUP_DATA_FILE_FORMAT % i_group
    all_group_data = np.loadtxt(file_name, delimiter=',')
    # make sure all values in the first column are zero
    assert(np.all(all_group_data[:, 0] == 0))
    # get and return only the valid part of the data
    group_data = all_group_data[:, VALID_DATA_COLUMN]
    return group_data
    

if __name__ == '__main__':
    # take a look at the data for the first group
    print(load_group_data(0))