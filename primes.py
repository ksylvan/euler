# Prime related utility methods.
#

from itertools import combinations, count
from math import prod
from os import path
from typing import List

from testing import report_timing, run_doctest, timer

__p = [2, 3, 5]

@timer
def next_prime(from_start: bool = False, limit: int = 0) -> int:
    """
    Generator that yields primes.
    
    If from_start=True, start from the beginning, else, yield the next prime.
    If limit is non-zero, stop at the given limit.
    
    >>> p = next_prime(from_start = True)
    >>> [next(p) for _ in range(5)]
    [2, 3, 5, 7, 11]
    >>> [next(p) for _ in range(2)]
    [13, 17]
    >>> p2 = next_prime()
    >>> [next(p2) for _ in range(3)]
    [19, 23, 29]
    >>> p = next_prime(from_start = True, limit = 10)
    >>> [i for i in p]
    [2, 3, 5, 7]
    """
    if from_start:
        for p in __p:
            if limit and p > limit:
                return
            yield p
    p = __p[-1] + 2
    while True:
        is_prime = True
        for i in count(1):
            if p % __p[i] == 0:
                is_prime = False
                break
            if __p[i] * __p[i] > p:
                break
        if is_prime:
            __p.append(p)
            yield p
        p += 2
        if limit and p > limit:
            break

@timer
def is_prime(n: int) -> bool:
    """
    Returns True if n is a prime number, False otherwise.
    
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(4)
    False
    >>> is_prime(41)
    True
    """
    if n < 2:
        return False
    p = next_prime(from_start = True)
    for v in p:
        if n == v:
            return True
        if n % v == 0:
            return False
        if v*v > n:
            break
    return True

@timer
def factors(n: int) -> List[int]:
    """
    Returns a list of all prime factors of n.
    
    >>> factors(2)
    [2]
    >>> factors(3)
    [3]
    >>> factors(0)
    []
    >>> factors(1)
    []
    >>> factors(4)
    [2, 2]
    >>> factors(44)
    [2, 2, 11]
    """
    res = []
    if n < 2:
        return []
    p = next_prime(from_start = True)
    while n > 1:
        for v in p:
            while n % v == 0:
                res.append(v)
                n //= v
            if v*v > n:
                break
        if v*v>n:
            break
    if n > 1:
        res.append(n)
    return res

@timer
def all_factors(n: int, include_one = False) -> List[int]:
    """
    Returns a list of all composite and prine factors of n.
    
    >>> all_factors(2)
    [2]
    >>> all_factors(24, include_one = True)
    [1, 2, 3, 4, 6, 8, 12, 24]
    """
    f = factors(n)
    res = set()
    if include_one:
        res.add(1)
    for i in range(1, len(f) + 1):
        for subset in combinations(f, i):
            res.add(prod(subset))
    return sorted(list(res))

@timer
def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.
    
    >>> gcd(2, 3)
    1
    >>> gcd(3, 2)
    1
    >>> gcd(0, 0)
    0
    >>> gcd(20, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    run_doctest()
    print(f"@ This utility module ({path.basename(__file__)}) does not answer any Euler project questions.")
    report_timing()