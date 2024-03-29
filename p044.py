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

from bisect import bisect_left
from itertools import count
from math import sqrt

from testing import report_timing, run_doctest, timer

@timer
def pent(n: int) -> int:
    """
    Returns the nth pentagonal number.
    
    >>> pent(1)
    1
    >>> pent(2)
    5
    """
    return n * (3*n - 1) // 2

@timer
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

@timer
def search(limit: int = 50000):
    """
    Generator that searches for a pentagonal number pair P(j) and P(k) such that
    k > j and P(k)-P(j) is a pentagonal number and P(k)+P(j) is also a pentagonal number.
    
    Suppose p(k) + p(j) = A, and
            p(k) - p(j) = B
    
    Then: p(k) = (A + B) / 2
          p(j) = (A - B) / 2
    
    So we can loop through the pentagonal numbers directly and only check if p(j)
    and p(k) are pentagonal or not when the possible value for B is smaller
    than the current number.
    """
    nums = [pent(i) for i in range(limit)]
    for i in range(2, limit):
        S = nums[i] # this represents A+B (the sum)
        for j in range(1, i - 1):
            diff = nums[j]
            pk = (S + diff)/2
            pj = (S - diff)/2
            if pentagonal_index(pk) != -1 and pentagonal_index(pj) != -1:
                yield (int(pj), int(pk))

if __name__ == "__main__":
    run_doctest()
    g = search()
    pj, pk = next(g)
    answer = pk - pj
    print(f"@ The answer to Euler #44 is {answer}")
    j = pentagonal_index(pj)
    k = pentagonal_index(pk)
    print(f"@ That answer corresponds to the pentagonal numbers at {j} and {k} index values.")
    report_timing()