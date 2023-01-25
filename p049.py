# Prime Permutations
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
#

from primes import next_prime, is_prime
from testing import report_timing, run_doctest, timer

@timer
def nDigitPrimes(n: int):
    """
    Return a generator for all the n-digit primes.
    
    >>> p = nDigitPrimes(1)
    >>> list(p)
    [2, 3, 5, 7]
    >>> p = nDigitPrimes(2)
    >>> list(p)
    [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> p = nDigitPrimes(3)
    >>> next(p)
    101
    """
    primes = next_prime(from_start=True)
    for i in primes:
        if i < 10**(n-1)-1:
            continue
        if i >= 10**n:
            break
        yield i

@timer
def digits(n) -> set[int]:
    """
    Return the number n as a set of digits.
    
    >>> digits(1)
    {1}
    >>> digits(209) == {0, 2, 9}
    True
    """
    digits = set()
    while n > 0:
        digits.add(n%10)
        n //= 10
    return digits

@timer
def getAnswer() -> str:
    """
    Generate the 12-digit number by concatenating the three terms in the
    sequence of 3 4-digit primes that are both monotonically increasing,
    and digital permutations of one another.
    """
    p = list(nDigitPrimes(4))
    n = len(p)
    res = []
    for i in range(n):
        for j in range(i+2, n):
            l, m, r = p[i], (p[i]+p[j])//2, p[j]
            if not is_prime(m):
                continue
            if (r-m) != (m-l):
                continue
            if digits(l) != digits(m) or digits(m) != digits(r):
                continue
            res.append([l,m,r])
    for s in res:
        if s[0] == 1487:
            continue
        return "".join(map(str, s))
        
if __name__ == "__main__":
    run_doctest()
    print(f"@ Answer for Euler #49: {getAnswer()}")
    report_timing()
    