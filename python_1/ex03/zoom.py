from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def zoom(path: str):
    
    arr = ft_load(path)

    plt.imshow(arr)
    plt.show()

    y1, y2 = 0, 500
    x1, x2 = 400, 900
    
    zoom_arr = arr[y1:y2, x1:x2]

    plt.imshow(zoom_arr)
    plt.show()

    print("New shape after slicing: ", zoom_arr.shape)

    return


if __name__ == "__main__":
    zoom("animal.jpeg")