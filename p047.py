# Distinct primes factors
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from primes import factors
from collections import Counter
from typing import List
from itertools import count

def distinct_primes(n: int) -> List[int]:
    """
    Find the first n consecutive integers that have n distinct prime factors.
    
    >>> distinct_primes(2)
    [14, 15]
    
    >>> distinct_primes(3)
    [644, 645, 646]
    """
    res = []
    for i in count(1):
        c = Counter(factors(i))
        if len(c) == n:
            res.append(i)
            if len(res) == n:
                break
        else:
            res = []
    return res
 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    answer = distinct_primes(4)
    print(f"@ The answer to Euler #47 is: {answer[0]}")
    print(f"@ The Four consequtive numbers with 4 distinct factors are: {answer}")