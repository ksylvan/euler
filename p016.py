# Power Digit Sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

def power_digit_sum(n: int) -> int:
    """
    Returns the sum of digits of 2^n
    
    >>> power_digit_sum(2)
    4
    >>> power_digit_sum(4)
    7
    >>> power_digit_sum(1000)
    1366
    """
    return sum(map(int, str(2**n)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print('@ Answer for Euler #16:', power_digit_sum(1000))