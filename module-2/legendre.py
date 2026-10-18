#------------------------------------------------------------------------------
# This module defines legpoly(), a fast calculation of Legendre polynomials.
#------------------------------------------------------------------------------

def legpoly(n,x):
    """Return value at x of ordinary Legendre Polynomial or degree n.

    This function implements the two-point recursion relation:
        (n + 1)P_{n+1}(x) = (2n + 1)xP_n(x) - nP_{n-1}(x)
    in a loop, without recursive calls to itself. This is the only efficient
    way to calculate values of Legendre polynomials of high degree.

    Parameters
    ----------
    n : nonnegative integer scalar
        Legendre polynomial degree
    x : real scalar in [-1,1]
        Legendre polynomial argument

    Returns
    -------
    y : real scalar
        Value of P_n at x
    """

    # Verify valid input
    assert (type(n) is int) and (n >= 0), "n must be nonnegative integer"
    assert (x >= -1) and (x <= 1), "x must be in [-1,1]" 

    # Calculate P_n(x)
    # TODO(human):
    #   1. Handle the starting cases: what are P_0(x) and P_1(x)?
    #      What should the function return right away if n is 0 or 1?
    #   2. Keep two variables for the two most recent polynomials,
    #      e.g. "previous" = P_{k-1} and "current" = P_k.
    #   3. Loop k from 1 up to n-1. On each pass, use
    #        P_{k+1} = ((2k+1) * x * P_k - k * P_{k-1}) / (k+1)
    #      to compute the next value.
    #   4. Shift the pair forward: the old "current" becomes "previous",
    #      and the new value becomes "current".
    #   5. After the loop, "current" holds P_n(x). Assign it to y.
    if n == 0:
        return 1.0
    if n == 1:
        return x
    p_prev = 1.0
    p_curr = x
    for k in range(1, n):
        p_next = ((2*k + 1)*x*p_curr - k*p_prev) / (k + 1)
        p_prev = p_curr
        p_curr = p_next
    y = p_curr

    return y

### For testing during development
def _test1():
    print("Testing legpoly implementation.")
    print()
    x = 0.5
    p0_true = 1.0
    p1_true = x
    p2_true = 0.5*(3*x**2 - 1)
    p3_true = 0.5*(5*x**3 - 3*x)
    p4_true = (1/8)*(35*x**4 - 30*x**2 + 3)
    print(f"Calculated P_0({x}) = {legpoly(0,x)}")
    print(f"Expected P_0({x}) = {p0_true}")
    print()
    print(f"Calculated P_1({x}) = {legpoly(1,x)}")
    print(f"Expected P_1({x}) = {p1_true}")
    print()
    print(f"Calculated P_2({x}) = {legpoly(2,x)}")
    print(f"Expected P_2({x}) = {p2_true}")
    print()
    print(f"Calculated P_3({x}) = {legpoly(3,x)}")
    print(f"Expected P_3({x}) = {p3_true}")
    print()
    print(f"Calculated P_4({x}) = {legpoly(4,x)}")
    print(f"Expected P_4({x}) = {p4_true}")
    print()
    print(f"Calculated P_3501({-1.0}) = {legpoly(3501,-1)}")
    print(f"Expected P_3501({-1.0}) = -1.0")

if __name__ == '__main__':
    print()
    _test1()
    print()
