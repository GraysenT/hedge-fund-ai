from numba import jit
@jit(nopython=True)
def fast_calc(x):
    return x * x