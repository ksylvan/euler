# Factorial Digit Sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#

from functools import reduce, cache
from operator import add
from math import prod
from testing import report_timing, run_doctest, timer

@timer
@cache
def factorial(n: int) -> int:
    if n == 0:
      return 1
    return prod(range(1, n+1))

@timer
def factorial_digit_sum(n: int) -> int:
    """
    Returns the sum of the digits of n!
    
    >>> factorial_digit_sum(10)
    27
    
    >>> factorial_digit_sum(20)
    54

    >>> factorial_digit_sum(30)
    117
    
    >>> factorial_digit_sum(100)
    648
    """
    return reduce(add, map(int, str(factorial(n))))

if __name__ == '__main__':
    run_doctest()
    print("@ Answer for Euler #20 (sum of digits in 100!):", factorial_digit_sum(100))
    report_timing()