# Self powers
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from testing import report_timing, run_doctest, timer

@timer
def self_powers(n: int, d: int) -> int:
    """
    Return the last d digits of n^n.
    
    >>> self_powers(1, 1)
    1
    >>> self_powers(3, 1)
    7
    """
    base = 10**d
    res = 1
    for i in range(1, n+1):
        res *= n
        res %= base
    return res

@timer
def self_powers_sum(n: int, d: int) -> int:
    """
    Return the last d digits of the sum of self powers up to n.
    
    >>> self_powers_sum(1, 1)
    1
    >>> self_powers_sum(2, 2)
    5
    >>> self_powers_sum(3, 2)
    32
    >>> self_powers_sum(10, 11)
    10405071317
    """
    res = 0
    for i in range(1, n+1):
        res += self_powers(i, d)
    return res % (10**d)

if __name__ == '__main__':
    run_doctest()
    answer = self_powers_sum(1000, 10)
    print("@ Answer to Euler #48:", answer)
    report_timing()