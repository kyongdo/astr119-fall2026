#------------------------------------------------------------------------------
# This module defines multitab() a multiplication table generator.
#------------------------------------------------------------------------------
import math

def multitab(n):
    """Print multiplication table up to n.

    Parameters
    ----------
    n : positive integer scalar

    Returns
    -------
    None
    """
    assert (type(n) is int) and (n > 0), "n must be positive integer"

    width = len(str(n * n)) + 1
    for row in range(1, n + 1):
        for column in range(1, n + 1):
            print(f"{row * column:{width}d}",end="")
        print()
    return None

### To run as a utility
if __name__ == '__main__':
    n = int(input("Multiplication table size: "))
    multitab(n)
