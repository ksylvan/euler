# Truncatable primes
#
# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
#
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from primes import is_prime, next_prime

def isTruncatablePrime(n: int) -> bool:
    """
    Returns True if the integer is a truncatable prime else False.
    
    >>> isTruncatablePrime(2)
    False
    >>> isTruncatablePrime(3)
    False
    >>> isTruncatablePrime(3797)
    True
    >>> isTruncatablePrime(73)
    True
    >>> isTruncatablePrime(79)
    False
    >>> isTruncatablePrime(3137)
    True
    >>> isTruncatablePrime(5000)
    False
    """
    if n < 11:
        return False
    s = str(n)
    for i in range(1, len(s)):
        num = int(s[i:])
        if not is_prime(num):
            return False
        num = int(s[:-i])
        if not is_prime(num):
            return False
    return True

if __name__ ==  "__main__":
    import doctest
    doctest.testmod(verbose=True)
    g = next_prime(from_start=True)
    s, num = 0, 11
    while num:
        p = next(g)
        if isTruncatablePrime(p):
            num -= 1
            s += p
    print(f"Euler Problem 36: The sum of the 11 truncatable primes is {s}")