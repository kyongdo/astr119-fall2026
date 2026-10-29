# pixels_extra.py -- Pod 5 extension: blur the moon

import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")


def blur(I):
    """Average each pixel with its four neighbors (up, down, left, right).

    I : array of shape (M, N, C), pixel values between 0 and 1.
    Returns an array of shape (M-2, N-2, C): the outermost ring of
    pixels is dropped, because those pixels are missing a neighbor.
    """
    # TODO(human):
    # 1. center = the pixels that have all four neighbors (drop 1 on every side)
    # 2. up, down, left, right = slices of I shifted by one pixel,
    #    each trimmed so its shape matches center exactly
    # 3. B = (center + up + down + left + right) / 5
    return B


if __name__ == "__main__":
    B = blur(I)
    print("original shape:", I.shape, " blurred shape:", B.shape)
    imsave("module-3/pixels_blur.png", B)
