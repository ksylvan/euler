# Combinatoric selections
#
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, ( 5 / 3) = 10
#
# In general, (n / r) = (n!)/((r!)*(n-r)!) where r<=n and
# n! is the product of all numbers from 1 to n (and 0! = 1)
#
# It is not until n = 23, that a value exceeds one-million: 
# (23 / 10) =  1144066
#
# How many, not necessarily distinct, values of (n / r)
# for 1 <= n <= 100 are greater than one million?

import math

from testing import report_timing, run_doctest, timer

@timer
def answer(lim: int, big: int) -> int:
    """Return the number of combnations (n choose r) for n <= lim,
    that are greater than 'big'
    
    >>> answer(6, 10)
    3
    """
    count = 0

    if lim < 1:
        return 0
    for n in range(1, lim + 1):
        for r in range(1, n+1):
            if math.comb(n, r) > big:
                count += n - 2*r + 1
                break
    return count

if __name__ == '__main__':
    run_doctest()
    ans = answer(100, 1000000)
    print("@ Euler #53  (Combinatoric selections) answer:", ans)
    report_timing()