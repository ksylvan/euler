# 1000-digit Fibonacci number
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
# The 12th term, F(12) is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from functools import cache

@cache
def fibonacci(n: int) -> int:
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(12)
    144
    """
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

def fib_term_with_digits(n: int):
    """
    >>> fib_term_with_digits(0)
    -1
    >>> fib_term_with_digits(1)
    0
    >>> fib_term_with_digits(2)
    7
    >>> fib_term_with_digits(1000)
    4782
    """
    if n <= 0:
        return -1
    elif n == 1:
        return 0
    lim = 10**(n-1)
    i = 0
    while fibonacci(i) < lim:
        i += 1
    return i

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)