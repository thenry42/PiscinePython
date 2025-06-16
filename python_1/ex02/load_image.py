import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """ to do """

    img = Image.open(path)
    arr = np.array(img)
    print("The shape of the image is: ", arr.shape)
    return arr