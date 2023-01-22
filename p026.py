# Reciprocal cycles
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from functools import cache
from typing import Tuple

from testing import report_timing, run_doctest, timer

@timer
@cache
def unit_fraction(n: int) -> Tuple[str, int]:
    """
    Return a tuple with a string and the length of the repeating cycle that is
    the decimal representation of the unit fraction.
    
    >>> unit_fraction(1)
    ('1', 0)
    >>> unit_fraction(2)
    ('0.5', 0)
    >>> unit_fraction(-3)
    ('-0.3', 1)
    >>> unit_fraction(7)
    ('0.142857', 6)
    """
    if n == 0:
        return ("NaN", 0)
    elif n < 1:
        s, rep = unit_fraction(-n)
        return ("-" + s, rep)
    elif n == 1:
        return ("1", 0)
    else:
        s = "0."
        x = 10
        hash_remainders = {}
        digit_place = 1
        while x > 0:
            d, r = divmod(x, n)
            if r in hash_remainders:
                prev = hash_remainders[r]
                return (s, digit_place - prev)
            hash_remainders[r] = digit_place
            s += str(d)            
            x = 10*r
            digit_place += 1
        return (s, 0)

@timer
@cache
def answer(n: int) -> int:
    """
    Try each unit fraction up to n and return the number that gives the largest fraction.
    
    >>> answer(10)
    7
    >>> answer(1000)
    983
    """
    if n <= 0:
        return -1
    saved_d, max_len, res = -1, -1, ""
    for d in range(n):
        s, l = unit_fraction(d)
        if l > max_len:
            saved_d, max_len, res = d, l, s
    return saved_d

if __name__ == "__main__":
    run_doctest()
    print(f"@ Answer to Euler 26: {answer(1000)}")          
    report_timing()