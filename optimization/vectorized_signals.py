import numpy as np
def signal_from_array(arr):
    return np.mean(arr) > np.median(arr)
