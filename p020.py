# Factorial Digit Sum
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#

from functools import reduce
from operator import add

def factorial(n: int) -> int:
    if n == 0:
      return 1
    else:
      return n * factorial(n - 1)

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
    import doctest
    doctest.testmod(verbose=True)