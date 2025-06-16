import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    """ Inverts the color of the image received. """
    new_array = []
    new_array[:] = 255 - array
    plt.imshow(new_array)
    plt.show()
    return


def ft_red(array) -> np.array:
    """ Keeps only the red color channel of the image. """
    new_array = array.copy()
    new_array[:, :, 1] = 0  # Set green channel to 0
    new_array[:, :, 2] = 0  # Set blue channel to 0
    plt.imshow(new_array)
    plt.show()
    return


def ft_green(array) -> np.array:
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0
    plt.imshow(new_array)
    plt.show()
    return


def ft_blue(array) -> np.array:
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0 
    plt.imshow(new_array)
    plt.show()
    return


def ft_grey(array) -> np.array:
    new_array = array.copy()

    grey_values = (new_array[:, :, 0] / 3 + 
                   new_array[:, :, 1] / 3 + 
                   new_array[:, :, 2] / 3 )

    new_array[:, :, 0] = grey_values
    new_array[:, :, 1] = grey_values
    new_array[:, :, 2] = grey_values
    
    plt.imshow(new_array)
    plt.show() 
    return