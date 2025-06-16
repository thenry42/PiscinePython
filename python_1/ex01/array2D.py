import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ to do """

    # 1. print the array
    arr = np.array(family)
    shape = arr.shape
    print("My shape is : ", shape)

    # 2. slice the  array
    arr = arr[start:end]
    shape = arr.shape
    print("My new shape is : ", shape)
    
    return(arr.tolist())

