# Quadratic primes
#
# Euler discovered the remarkable quadratic formula:
#
# n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer values
# 0 <= n <= 39. However, when n=40, n^2+n+41 is divisible by 41, and certainly when  n=41,
# the result is clearly divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the 
# consecutive values 0 <= n <= 79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n^2 + an + b
#
# where abs(a)<1000 and abs(b)<=1000
#
# Find the product of the coefficients, a, b for the quadratic expression that produces the
# maximum number of primes for consecutive values of n starting with n=0
#

from functools import cache
from itertools import count
from typing import Tuple

from primes import is_prime
from testing import report_timing, run_doctest, timer

@timer
def quadratic(a: int, b: int, n: int) -> int:
    return n**2 + a*n + b

@timer
def num_of_primes(a: int, b:int) -> int:
    for i in count(0):
        if not is_prime(quadratic(a, b, i)):
            break
    return i

@timer
@cache
def find_a_b(N: int) -> Tuple[int, int]:
    """
    Find a and b between -N to N+1 that maximize the sequence of primes.
    
    >>> find_a_b(10)
    (-3, 7)
    >>> find_a_b(100)
    (-15, 97)
    >>> find_a_b(1000)
    (-61, 971)
    """
    t = (-1, 0, 0)
    for i in range(-N, N+1):
        if i % 2 == 0:
            continue
        for j in range(-N, N+1):
            if not is_prime(j):
                continue
            k = (num_of_primes(i, j), i, j)
            # if k[0] > 30: print(f"n^2 + {i}n + {j} -> {k[0]}")
            t = max(t, k)
    return (t[1], t[2])

if __name__ == "__main__":
    run_doctest()
    a, b = find_a_b(1000)
    print (f"@ Project Euler Problem 27 answer: {a*b}")
    report_timing()