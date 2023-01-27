# Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from typing import Tuple

from primes import next_prime, is_prime
from testing import report_timing, run_doctest, timer

@timer
def longestConsecutiveSumOfPrimes(n: int) -> Tuple[int, int, int]:
    """
    Find the longest sum of consecutive primes below n that adds to a prime.
    Returns the sum, the length of the sequence, and the starting prime.

    >>> longestConsecutiveSumOfPrimes(100)
    (41, 6, 2)
    >>> longestConsecutiveSumOfPrimes(1000)
    (953, 21, 7)
    >>> longestConsecutiveSumOfPrimes(10000)
    (9521, 65, 3)
    """
    p = next_prime(from_start=True)
    primes = []
    for i in p:
        if i > n:
            break
        primes.append(i)
    sums = [0] * (len(primes) + 1)
    for i in range(1, len(primes) + 1):
        sums[i] = sums[i-1] + primes[i-1]
    
    primes_set = set(primes)
        
    max_length = 0
    result_sum = 0
    result_start = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            curr_sum = sums[j + 1] - sums[i]
            if curr_sum >= n:
                break
            if curr_sum in primes_set and j - i + 1 > max_length:
                max_length = j - i + 1
                result_sum = curr_sum
                result_start = primes[i]
    return result_sum, max_length, result_start             

if __name__ == '__main__':
    run_doctest()
    resulting_sum, seq_len, starting_prime = longestConsecutiveSumOfPrimes(1000000)
    print(f"@ Euler Problem 50 answer: {resulting_sum}")
    print(f"@ The sequence has {seq_len} terms, starting at {starting_prime}")
    report_timing()