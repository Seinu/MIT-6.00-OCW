# 6.00 Problem Set 2
#
# Successive Approximation
#
# Name: seinu
# Collaborators (Discussion): None
# Collaborators (Identical Solution): None
# Notes: was confused with reimplementing basic math for first 2 functions(without them) for compute_root
#   before realizing that I just needed to utilize them in the math after checking solution for help
# Time: 6:00
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2 + 0(-13)^1 + 0(-13)^0
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    y = 0.0
    if len(poly) <= 0:
        return None
    else:
        for i in range(len(poly)):
           y += poly[i]*x**i
            
        
    return y

def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    y = ()
    c = 0.0
    if len(poly) <= 0:
        return None
    else:
        for i in range(1, len(poly)):
            if poly[i] == 0.0:
                y = y + (0.0,)
            else:
                c = poly[i] * i
                y = y + (c,)
            c = 0.0
                
    return y

def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    count = 1
    x = x_0
    while abs(evaluate_poly(poly, x)) >= epsilon:
        x = (x - evaluate_poly(poly, x)/evaluate_poly(compute_deriv(poly), x))
        count += 1
    return (x, count)
            


