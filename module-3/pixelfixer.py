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

    bad_count = 0

    for i in range(rows):
        for j in range(cols):

            if (I[i, j, 0] == 1 and
                I[i, j, 1] == 0 and
                I[i, j, 2] == 0):

                bad_count += 1
                I[i, j] = [1, 1, 1]   # paint the bad pixel white

    print("Bad pixels found:", bad_count)

    return I


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
