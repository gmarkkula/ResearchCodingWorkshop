# generate some artifical data for the examples

import numpy as np
from numpy.random import default_rng
import my_module


N_MEASUREMENTS_PER_GROUP = 20
N_DATA_COLS = 2 # including an extra, unused column of data
DATA_STD_DEV = 1

# initialise random number generator
rng = default_rng()

# generate artificial data
for i_group in range(my_module.N_GROUPS):
    # just a dummy function describing the true mean of the underlying data
    true_mean = 3  + i_group ** 2
    # get noisy data
    noisy_data = rng.normal(loc=true_mean, scale=DATA_STD_DEV, 
                            size=(N_MEASUREMENTS_PER_GROUP, N_DATA_COLS))
    # all zeros in the first column
    noisy_data[:, 0] = 0
    # save file
    print(noisy_data)    
    np.savetxt(my_module.GROUP_DATA_FILE_FORMAT % i_group, noisy_data, 
               delimiter=',')