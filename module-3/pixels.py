# pixels.py -- Pod 5: Pixels Are Numbers

import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("module-3/clean_io_small.png")

if __name__ == "__main__":
    print("shape:", I.shape)

    # TASK 1: HOW MANY NUMBERS?
    print("Total numbers:", I.size)

    # TASK 1: TWO PIXELS
    print("Top-left pixel:", I[0, 0])
    print("Middle pixel:", I[356, 349])

    # TASK 1: DRAW ON THE PICTURE
    J = I.copy()

    # Make a white square in the corner
    J[20:40, 20:40, :] = 1

    # Make a black line across the middle
    J[356, :, :] = 0

    # Save the edited picture
    imsave("module-3/pixels_out.png", J)

    # TASK 2: MAKE IT YOURS (WHITE FRAME)
    K = I.copy()

    # Top border
    K[:10, :, :] = 1

    # Bottom border
    K[-10:, :, :] = 1

    # Left border
    K[:, :10, :] = 1

    # Right border
    K[:, -10:, :] = 1

    # Save your new picture
    imsave("module-3/pixels_frame.png", K)



# TASK 2: PURPLE MOON

P = I.copy()

# Keep the red channel
P[:, :, 0] = I[:, :, 0] * 0.7

# Reduce the green channel
P[:, :, 1] = I[:, :, 1] * 0.2

# Increase the blue channel
P[:, :, 2] = I[:, :, 2] * 0.9

# Save the purple moon
imsave("module-3/pixels_purple.png", P)