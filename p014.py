# Largest Collatz sequence 
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million
#

from functools import cache

from testing import report_timing, run_doctest, timer

@timer
@cache
def collatz_length(n: int) -> int:
    """
    >>> collatz_length(1)
    1
    >>> collatz_length(2)
    2
    >>> collatz_length(3)
    8
    >>> collatz_length(13)
    10
    """
    if n == 1:
        res = 1
    else:
        if n % 2 == 0:
            res = collatz_length(n // 2) + 1
        else:
            res = collatz_length(3 * n + 1) + 1
    return res

@timer
@cache
def collatz_longest_sequence_under(n: int) -> int:
    """
    >>> collatz_longest_sequence_under(1)
    1
    >>> collatz_longest_sequence_under(20)
    18
    >>> collatz_longest_sequence_under(1000000)
    837799
    """
    num, max_length = 1, collatz_length(1)
    for i in range(1, n):
        l = collatz_length(i)
        if l > max_length:
            max_length = l
            num = i
    return num

if __name__ ==  "__main__":
    run_doctest()
    print(f"@ Answer to Euler #14: {collatz_longest_sequence_under(1000000)}")
    report_timing()