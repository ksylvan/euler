# Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
# exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
# multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written 
# as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it
# once in your sum.

from typing import Set

from primes import all_factors
from testing import report_timing, run_doctest, timer

@timer
def pandigital_product() -> Set[int]:
    """
    Return the list of products C, where A*B=C and ABC together have all digits from 1-9.
    
    We can use a crude factorization to create factors of C and only check those
    for values of A and B.
    
    >>> s = pandigital_product()
    >>> 7254 in s
    True
    """
    res = set()
    # Iterate through all possiblevalues of C
    for C in range(100, 10000):
        # Find the factors of C
        factors = all_factors(C, include_one = False)
        # Check for pandigital-ness
        for A in factors:
            B = C // A
            if ''.join(sorted(str(A)+str(B)+str(C))) == '123456789':
                res.add(C)
    return res

if __name__ == '__main__':
    run_doctest()
    s = pandigital_product()
    print("@ Euler 32 answer:", sum(s))
    print(f"@ The set of numbers is: {s}")
    report_timing()