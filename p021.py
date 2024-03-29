# Amicable Numbers
#
# https://en.wikipedia.org/wiki/Amicable_numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
# amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from functools import cache, reduce
from itertools import combinations
from math import sqrt
from operator import mul
from typing import List

from testing import report_timing, run_doctest, timer

odd_primes = [3, 5]

@timer
def prime_generator() -> int:
    p = odd_primes[-1] + 2
    while True:
        is_prime = False
        k = int(sqrt(p)) + 1
        for v in odd_primes:
            if p % v == 0:
                break
            elif v > k:
                is_prime = True
                break
        if is_prime:
            odd_primes.append(p)
            yield p
        p += 2
  
@timer
def factors(n: int) -> List[int]:
    """Return list of prime factors of n.
    
    >>> factors(1)
    []
    >>> factors(2)
    [2]
    >>> factors(9)
    [3, 3]
    >>> factors(7865)
    [5, 11, 11, 13]
    """
    result = []
    g = prime_generator()
    while n%2 == 0:
        result.append(2)
        n = n//2
    k = int(sqrt(n)) + 1
    for v in odd_primes:
        while n%v == 0:
            result.append(v)
            n //= v
        if v > k:
            break
    while n > 1:    
        v = next(g)
        while n > v and n%v == 0:
            result.append(v)
            n //= v
        if v >= n and n > 1:
            result.append(n)
            n = 1
    return result

@timer
def gen_proper_divisors(d: List[int]) -> List[int]:
    """Return list of proper divisors of d.
    
    >>> gen_proper_divisors([2, 2, 5, 11])
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    """
    res = set([1])
    for i in range(1, len(d)):
        for c in combinations(d, i):
            res.add(reduce(mul, c))
    return sorted(list(res))

@timer
def sum_proper_factors(n: int) -> int:
    """
    Return the sum of all proper factors of n.

    >>> sum_proper_factors(1)
    0
    
    >>> sum_proper_factors(2)
    1
    
    >>> sum_proper_factors(220)
    284
    """
    if n <= 0:
        return -1
    if n == 1:
        return 0
    return sum(gen_proper_divisors(factors(n)))

@timer
@cache
def is_amicable(n: int) -> bool:
    """
    Return True if n is a amicable number.

    >>> is_amicable(1)
    False
    >>> is_amicable(220)
    True
    >>> is_amicable(284)
    True
    >>> is_amicable(285)
    False
    """
    if n < 1:
        return False
    n1 = sum_proper_factors(n)
    n2 = sum_proper_factors(n1)
    return n2 == n and n1 != n2

@timer
@cache
def all_amicable_under(lim: int) -> int:
    """
    Return the sum of all amicable numbers under lim.

    >>> all_amicable_under(1)
    0
    >>> all_amicable_under(1000)
    504
    >>> all_amicable_under(5000)
    8442
    >>> all_amicable_under(10000)
    31626
    """
    s = 0
    for i in range(1, lim):
        if is_amicable(i):
            s += i
    return s

if __name__ == "__main__":
    run_doctest()
    print("@ The answer to Euler #21 (sum of all amicable numbers under 10000):", all_amicable_under(10000))
    report_timing()