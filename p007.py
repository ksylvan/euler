# 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from math import sqrt

primes = [2, 3, 5, 7, 11, 13]

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    k = int(sqrt(n)) + 1
    for i in primes:
        if n % i == 0:
            return False
        if i >= k:
            return True

def nthPrime(n: int) -> int:
    """
    Returns the nth prime number
    >>> nthPrime(1)
    2
    >>> nthPrime(2)
    3
    >>> nthPrime(3)
    5
    >>> nthPrime(4)
    7
    >>> nthPrime(5)
    11
    >>> nthPrime(6)
    13
    >>> nthPrime(23)
    83
    >>> nthPrime(10001)
    104743
    """
    nPrimes = len(primes)

    if n <= nPrimes:
        return primes[n - 1]
    k = primes[-1] + 2
    while nPrimes < n:
        while not isPrime(k):
            k += 2
        primes.append(k)
        nPrimes += 1
        k += 2
    return primes[n - 1]

#
# Test cases
#
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)