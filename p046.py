# Goldbach's other conjecture
#
# It was proposed by Christian Goldbach that every odd composite 
# number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#

from primes import is_prime
from math import sqrt
from itertools import count

def is_goldbach(n: int) -> bool:
    """
    Returns true if n works with the goldbach formula.
    
    >>> is_goldbach(9)
    True
    >>> is_goldbach(15)
    True
    >>> is_goldbach(21)
    True
    >>> is_goldbach(25)
    True
    >>> is_goldbach(27)
    True
    """
    if is_prime(n):
        return True
    for i in range(1, int(sqrt(n/2))+1):
        if is_prime(n - 2*i**2):
            return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)  
    for n in count(9, 2):
        if not is_goldbach(n):
            break
    print("@ The answer to Euler #46 is", n)
