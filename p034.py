# Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from typing import Dict, List

def digit_factorials() -> Dict[int, int]:
    """
    >>> digit_factorials()
    {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    """
    h = {0: 1}
    f = 1
    for i in range(1, 10):
        f *= i
        h[i] = f
    return h

def find_digit_factorial_nums() -> List[int]:
    fact_hash = digit_factorials()
    res = []
    for i in range(3, 1000000):
        s, n = 0, i
        while n:
            s += fact_hash[n % 10]
            n //= 10        
        if s == i:
            res.append(i)
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(f"Euler 34 answer: {sum(find_digit_factorial_nums())}")