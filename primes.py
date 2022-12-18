# Prime related utility methods.
#

from itertools import count
from typing import List

__p = [2, 3, 5]

def next_prime(from_start: bool = False) -> int:
    """
    Generator that yields primes.
    
    If from_start=True, start from the beginning, else, yield the next prime.
    
    >>> p = next_prime(from_start = True)
    >>> [next(p) for _ in range(5)]
    [2, 3, 5, 7, 11]
    >>> [next(p) for _ in range(2)]
    [13, 17]
    >>> p2 = next_prime()
    >>> [next(p2) for _ in range(3)]
    [19, 23, 29]
    """
    if from_start:
        for p in __p:
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

def factors(n: int) -> List[int]:
    """
    Returns a list of all prime numbers of n.
    
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
    import doctest
    doctest.testmod(verbose=True)