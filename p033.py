# Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from typing import List, Tuple

from primes import gcd
from testing import report_timing, run_doctest, timer

@timer
def digit_canceling_fractions() -> List[Tuple[int,int]]:
    """
    Return the list of non-trivial digit-canceling fractions
    
    The idea is that we have cases where we have a two digit number 10a+b and another 10b+c
    where 0 < a < 10, and the same for b and c. And 10a+b/10b+c == a/c
    
    >>> l = digit_canceling_fractions()
    >>> (49, 98) in l
    True
    """
    res = []
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if a == b and a == c:
                    continue
                if (10*a+b)/(10*b+c) == a/c:
                    res.append((10*a+b, 10*b+c))
    return res

if __name__ == "__main__":
    run_doctest()
    numerator, denominator = 1, 1
    print("@ The list of two-digit digit canceling fractions are:")
    for a, b in digit_canceling_fractions():
        print(f"@ {a}/{b}")
        numerator *= a
        denominator *= b
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    print(f"@ The product of those fractions, normalized is: {numerator}/{denominator}")
    print(f"@ The answer to Euler 33 is: {denominator}")
    report_timing()