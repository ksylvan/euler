# Lexicographic permutations
#
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from typing import List
from functools import reduce

# https://en.wikipedia.org/wiki/Factorial_number_system#Permutations
#


def fact(n: int) -> int:
    """
    Return the nth factorial number.
    
    >>> fact(0)
    1
    >>> fact(4)
    24
    >>> fact(5)
    120
    >>> fact(6)
    720
    """
    if n == 0:
        return 1
    return reduce(lambda a, b: a * b, range(1, n + 1))


def factoradic(n: int) -> List[int]:
    l, i = [0], 2
    while n:
        n, remainder = divmod(n, i)
        l.append(remainder)
        i += 1
    l.reverse()
    return l


def nth(n: int, s: str) -> str:
    """
    >>> nth(100, '01234')
    '40231'
    
    >>> nth(1000000, '0123456789')
    '2783915460'
    """
    l = factoradic(n - 1)
    l = [0] * (len(s) - len(l)) + l
    c = s[:]
    res = []
    for i in range(len(s)):
        res.append(c[l[i]])
        c = c.replace(c[l[i]], "")
    return "".join(res)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)