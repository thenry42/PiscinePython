from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def rotate(path: str):

    # 1. load the image
    img_arr = ft_load(path)
    print(img_arr)

    # 2. Slice the image    
    y1, y2 = 0, 500
    x1, x2 = 400, 900
    zoom_arr = img_arr[y1:y2, x1:x2]
    print("The shape of the image is: ", zoom_arr.shape)

    # 3. rotate the image using custom transpose
    transposed = []
    rows = len(zoom_arr)
    cols = len(zoom_arr[0])
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(zoom_arr[i][j])
        transposed.append(new_row)    

    print(np.array(transposed).shape)

    plt.imshow(transposed)
    plt.show()

    return


if __name__ == "__main__":
    rotate("animal.jpeg")