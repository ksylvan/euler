# Pentagon numbers
#
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
# However, their difference, 70 − 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
# and D = |Pk − Pj| is minimised; what is the value of D?
#

from math import sqrt
from itertools import count
from bisect import bisect_left

def pent(n: int) -> int:
    """
    Returns the nth pentagonal number.
    
    >>> pent(1)
    1
    >>> pent(2)
    5
    """
    return n * (3*n - 1) // 2

def pentagonal_index(x: int) -> int:
    """
    Returns a positive integer n if x is a pentagonal number.
    else returns -1.
    
    >>> pentagonal_index(1)
    1
    >>> pentagonal_index(5)
    2
    >>> pentagonal_index(12)
    3
    >>> pentagonal_index(35)
    5
    >>> pentagonal_index(51)
    6
    >>> pentagonal_index(30)
    -1
    >>> pentagonal_index(45)
    -1
    """
    # https://en.wikipedia.org/wiki/Pentagonal_number
    # Given a positive integer x, to test whether it is a pentagonal number we can compute
    # using the quadratic formula:
    #   2x = n(3n -1), so 3n^2 - n - 2x = 0
    # So the two roots are:
    #   n = (1 +/- sqrt(1 + 24x))/6
    # The positive root is
    #   n = (1 + sqrt(1 + 24x))/6
    # So to test whether n is a pentagonal number we only have to see if the n from the above formula
    # is a natural number.
    n = (1+ sqrt(1+24*x))/6
    return int(n) if n == int(n) else -1

def search():
    """
    Generator that searches for a pentagonal number pair P(m) and P(n) such that
    n > m and P(n) - P(m) is a pentagonal number and P(n)+P(m) is also a pentagonal number.
    """
    for n in count(2):
        p_n = pent(n)
        for m in range(1, n):
            p_m = pent(m)
            if pentagonal_index(p_n - p_m) != -1 and pentagonal_index(p_m + p_n) != -1:
                yield (p_m, p_n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    g = search()
    pj, pk = next(g)
    answer = pk - pj
    print(f"@ The answer to Euler #44 is {answer}")
    j = pentagonal_index(pj)
    k = pentagonal_index(pk)
    print(f"@ That answer corresponds to the pentagonal numbers at {j} and {k} index values.")