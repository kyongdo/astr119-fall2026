
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

    for i in range(rows):
        for j in range(cols):

            if (I[i, j, 0] == 1 and
                I[i, j, 1] == 0 and
                I[i, j, 2] == 0):

                neighbors = []

                if i > 0:
                    neighbors.append(I[i - 1, j])

                if i < rows - 1:
                    neighbors.append(I[i + 1, j])

                if j > 0:
                    neighbors.append(I[i, j - 1])

                if j < cols - 1:
                    neighbors.append(I[i, j + 1])

                average = np.mean(neighbors, axis=0)

                fixed[i, j] = average

    return fixed

### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
### 1. Bad Pixels found: 4840
### 2. Every red dot becomes white (same spots)
### 3. The dots blend into their surroundings (623 still differ from the
###    clean image by more than 0.02)


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()

