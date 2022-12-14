# Non-abundant sums
#
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
# is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and
# it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from p021 import sum_proper_factors

def is_abundant(n: int) -> bool:
    """
    >>> is_abundant(12)
    True

    """
    return sum_proper_factors(n) > n

def solve() -> int:
    """
    Returns the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

    Everything beyond 28123 has been proven to be the sum of two abundant numbers, so we only
    need to generate a list of all abundant numbers below 28123 and then combine them to see the list
    of all numbers possible to represent as the sum of two abundant numbers, and use that to derive the answer.

    >>> solve()
    4179871
    """
    lower_limit = 28124
    abundants = []
    for i in range(lower_limit):
        if is_abundant(i):
            abundants.append(i)
    abundants_len = len(abundants)
    l = {}
    for i in range(abundants_len):
        for j in range(abundants_len):
            l[abundants[i] + abundants[j]] = True
    res = 0
    for i in range(lower_limit + 1):
        if i not in l:
            res += i
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)