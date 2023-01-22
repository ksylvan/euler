# Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# Given that a 0-digit pandigital number would contain all 9 numbers and is therefore divisible by 3 and nonprime,
# we can start by looking only at 8-digit pandigital combinations and test for primeness.

from functools import reduce
from itertools import permutations

from primes import is_prime
from testing import report_timing, run_doctest, timer

@timer
def largest_pandigital_prime(n: int) -> int:
    """
    Returns largest pandigital prime n-digit number.
    
    If no such prime exists, return -1.
    
    >>> largest_pandigital_prime(1)
    -1
    >>> largest_pandigital_prime(2)
    -1
    >>> largest_pandigital_prime(9)
    -1
    >>> largest_pandigital_prime(4)
    4231
    """
    c = permutations(reversed(range(1, n+1)))
    for i in c:
        n = reduce(lambda x, y: 10*x + y, i)
        if is_prime(n):
            return n
    return -1

if __name__ == "__main__":
    run_doctest()
    answer = None
    for i in reversed(range(1, 10)):
        x = largest_pandigital_prime(i)
        if x != -1:
            answer = x
            break
    print(f"@ The answer to Euler #41 is {answer}")
    report_timing()