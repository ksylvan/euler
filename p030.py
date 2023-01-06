# Digit fifth powers
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers
# of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
#
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from typing import List
from functools import cache

max_num = 10**6 - 1

@cache
def findArmstrongLikeNumbers(n: int) -> List[int]:
    """
    There are only 3 known Armstrong numbers (sum of 4th power of their digits)

    >>> findArmstrongLikeNumbers(4)
    [1634, 8208, 9474]
    >>> findArmstrongLikeNumbers(3)
    [153, 370, 371, 407]
    >>> findArmstrongLikeNumbers(2)
    []
    >>> findArmstrongLikeNumbers(5)
    [4150, 4151, 54748, 92727, 93084, 194979]
    """
    h = {i: i**n for i in range(10)}
    res = []
    for i in range(2, max_num + 1):
        s = sum([h[int(k)] for k in str(i)])
        if s == i:
            res.append(i)
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    l = findArmstrongLikeNumbers(5)
    print("@ Euler Project #30 answer:", sum(l))
    print(f"@ The numbers that make up ths sum: {l}")
