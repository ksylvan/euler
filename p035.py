# Circular primes
#
# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from primes import is_prime
from typing import Set

from testing import report_timing, run_doctest, timer

@timer
def rotate_number(n: int) -> int:
    """
    >>> rotate_number(23)
    32
    >>> rotate_number(127)
    712
    >>> rotate_number(3456)
    6345
    >>> rotate_number(-8)
    -8
    >>> rotate_number(0)
    0
    """
    if n < 0:
        return -rotate_number(-n)
    if n < 10:
        return n
    return int(str(n % 10) + str(n //10))

@timer   
def check_circular(n: int, r: Set[int] = None) -> int:
    """
    Return the number of circular primes given a starting number in the cycle.
    Also adds the primes to the set() if that parameter is given.
    
    >>> check_circular(0)
    0
    >>> check_circular(1)
    0
    >>> check_circular(2)
    1
    >>> check_circular(3)
    1
    >>> check_circular(4)
    0
    >>> check_circular(31)
    2
    >>> check_circular(197)
    3
    """
    if not is_prime(n):
        return 0
    if n > 7:
        s = str(n)
        for d in '024685':
            if d in s:
                return 0
    c = set([n])
    num_of_primes = 1
    n = rotate_number(n)
    while n not in c:
        c.add(n)
        num_of_primes += 1
        if not is_prime(n):
            return 0
        n = rotate_number(n)
    if r is not None:
        r |= c
    return num_of_primes

@timer
def circular_primes_below(n: int, res: Set[int] = None) -> int:
    """
    Returns the number of circular primes below n.
    
    >>> r = set()
    >>> circular_primes_below(10, r)
    4
    >>> r
    {2, 3, 5, 7}
    >>> circular_primes_below(100)
    13
    """
    num = 1
    if res is not None:
        res.add(2)
    else:
        res = set([2])
    for p in range(3, n, 2):
        if p not in res and is_prime(p):
            num += check_circular(p, res)
    return len(res)

if __name__ ==  "__main__":
    run_doctest()
    r = set()
    n = circular_primes_below(1000000, r)
    print("@ Euler 35 answer for how many circular primes below a million:", n)
    print(f"@ The set of circular primes is: {sorted(list(r))}")
    report_timing()