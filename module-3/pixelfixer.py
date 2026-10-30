#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave




def pixelfix(I):

    rows, cols, colors = I.shape

    fixed = I.copy()

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            if (I[i, j, 0] == 1 and
                I[i, j, 1] == 0 and
                I[i, j, 2] == 0):

                up = I[i - 1, j]
                down = I[i + 1, j]
                left = I[i, j - 1]
                right = I[i, j + 1]

                average = (up + down + left + right) / 4

                fixed[i, j] = average

    return fixed



    ### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
    ### 1. find the bad pixels and print how many;
    ### 2. paint them white and look at the result;
    ### 3. replace the white with the average of the up/down/left/right
    ###    neighbors. Then try solo_corrupt_io_small.png.)

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
