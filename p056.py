# Powerful digit sum
#
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, a^b, where a, b < 100,
# what is the maximum digital sum?

from typing import Tuple

from testing import run_doctest, report_timing, timer

@timer
def digit_sum(n: int) -> int:
    """Computes the digit sum of a positive integer.
    
    >>> digit_sum(0)
    0
    >>> digit_sum(123)
    6
    """
    return sum(int(digit) for digit in str(n))

@timer
def max_digit_sum(limit: int) -> Tuple[int, int, int]:
    """Return the max digit sum and the powers that generate that, given a limit.
    
    >>> max_digit_sum(10)
    (9, 7, 45)
    """
    max_digit_sum = 0
    powers = None

    for a in range(1, limit):
        for b in range(1, limit):
            digit_sum_ab = digit_sum(a**b)
            if digit_sum_ab > max_digit_sum:
                max_digit_sum = digit_sum_ab
                powers = (a, b)
    return powers + (max_digit_sum,)

if __name__ == '__main__':
    run_doctest()
    ans = max_digit_sum(100)
    print(f"@ Euler #56 answer is {ans[2]}, which is {ans[0]}**{ans[1]}")
    report_timing()