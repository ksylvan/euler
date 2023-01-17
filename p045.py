# Triangular, pentagonal, and hexagonal
#
# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	T(n)=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	P(n)=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	H(n)=n(2n−1)	 	1, 6, 15, 28, 45, ...
#
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

from math import sqrt
from itertools import count

def isTriangle(x: int) -> bool:
    """
    Returns True if x is a triangle number, False otherwise.
    
    >>> isTriangle(1)
    True
    >>> isTriangle(2)
    False
    >>> isTriangle(3)
    True
    >>> isTriangle(10)
    True
    >>> isTriangle(12)
    False
    """
    # Apply the quadratic formula.
    # n^2 + n - 2x = 0
    #
    # n = (-1 +- sqrt(1 + 8x))/2
    #
    
    n = (-1 + sqrt(1 + 8 * x)) / 2
    return n == int(n)

def isPentagonal(x: int) -> bool:
    """
    Returns True if x is a pentagonal number, False otherwise.
    
    >>> isPentagonal(1)
    True
    >>> isPentagonal(2)
    False
    >>> isPentagonal(5)
    True
    """
    n = (1+ sqrt(1+24*x))/6
    return n == int(n)

def hexagonal(n: int) -> int:
    """
    Returns the nth hexagonal number.
    
    >>> hexagonal(1)
    1
    >>> hexagonal(2)
    6
    >>> hexagonal(3)
    15
    >>> hexagonal(4)
    28
    """
    return n*(2*n - 1)

def next_hexPentTri(starting: int = 1):
    """
    Generate the next triangle number that is also pentagonal and hexagonal.
    
    >>> g = next_hexPentTri()
    >>> next(g)
    1
    >>> next(g)
    40755
    """
    for i in count(starting):
        h = hexagonal(i)
        if isPentagonal(h) and isTriangle(h):
            yield h      

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    g = next_hexPentTri()
    for h in g:
        if h > 40755:
            ans = h
            break
    print(f"@ Answer to Euler #45 is {ans}")