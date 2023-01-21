# Largest prime factor
#
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

from math import sqrt
from typing import List

from testing import report_timing, run_doctest, timer

@timer
def factors(n: int) -> List[int]:
    f = []
    while n%2 == 0:
        f.append(2)
        n //= 2
    for prime in range(3, int(sqrt(n)) + 1, 2):
        if n % prime == 0:
            f.append(prime)
            n //= prime
    if n > 1:
        f.append(n)
    return f

@timer
def largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of the number n.

    >>> largest_prime_factor(6)
    3
    >>> largest_prime_factor(13)
    13
    >>> largest_prime_factor(33)
    11
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(600851475143)
    6857
    """
    
    r = factors(n)
    return max(r)        
    
if __name__ == "__main__":
    run_doctest()
    print('@ Answer to Euler #3:', largest_prime_factor(600851475143))
    report_timing()