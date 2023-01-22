# Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from math import sqrt

from testing import report_timing, run_doctest, timer

primes = [2, 3, 5, 7, 11, 13, 17, 19]

@timer
def generate_primes():
    p = len(primes)
    for i in range(p):
        yield primes[i]
    candidate = primes[-1] + 2
    while True:
        is_prime = True
        up_to = int(sqrt(candidate)) + 1
        for v in primes:
            if v >= up_to:
                break
            if candidate % v == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
            primes.append(candidate)
        candidate += 2

@timer
def sum_of_primes_below(n: int) -> int:
    """
    Returns the sum of the primes below n.
    
    >>> sum_of_primes_below(10)
    17
    >>> sum_of_primes_below(15)
    41
    >>> sum_of_primes_below(1000)
    76127
    >>> sum_of_primes_below(1000000)
    37550402023
    >>> sum_of_primes_below(2 * 1000000)
    142913828922
    """
    res = 0
    for p in generate_primes():
        if p >= n:
            break
        res += p
    return res

if __name__ == '__main__':
    run_doctest()
    print('@ Answer to Euler #10:', sum_of_primes_below(2 * 1000000))
    report_timing()