# Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#

# Approach: 9 1 digit numbers +
#           10-99 (90 two digit numbers) + 
#           100-999 (900 three digit numbers) +
#           1000-9999 (9000 four digit numbers) + [...]

# So there are 9*10^(n-1) n-digit number spans in the fractional part.
# Making each span of numbers have a length of 9*n*10^(n-1)
#
# So in order to find the kth digit, we have to work
# backward. We find out which span the number is in (1-digit numbers,
# 2 digit numbers, etc.)
#
# So, 9 1-digit numbers = 9
# 9*10^1 = 90 2-digit numbers = 180 digits [10-99 in digits 10-180]
# 9*10^2 = 900 3-digit numbers = 2700 digits
# 9*10^3 = 9000 4-digit numbers = 36000 digits
# etc.

from math import prod

from testing import report_timing, run_doctest, timer

@timer
def s(n: int, lim=1000000) -> str:
    res = "-"
    for i in range(1, n):
        res += str(i)
        if len(res) > lim:
            break
    return res

@timer
def d(n: int) -> int:
    """
    Return the nth digit of the fractional part of Champernowne's constant
    in base 10.
    
    >>> d(0)
    -1
    >>> d(-1)
    -1
    >>> d(1)
    1
    >>> d(7)
    7
    >>> d(12)
    1
    >>> d(2711)
    4
    >>> d(6754)
    1
    >>> x = s(1000)
    >>> x[765] == str(d(765))
    True
    """
    if n < 1:
        return -1
    
    digit_spans = {}
    digit_spans[0] = 1
    increments = {}
    increments[0] = 1
    for j in range(1, 10):
        digit_spans[j] = digit_spans[j-1] + j*9*(10**(j-1))
        increments[j] = 10**j
    for j in range(1, 10):
        if n < digit_spans[j]:
            n -= digit_spans[j-1]
            k = increments[j-1] + n // j # the number we are at
            digit_position = n % j
            return int(str(k)[digit_position])
            
    return 0

if __name__ == "__main__":
    run_doctest()
    j = [1, 10, 100, 1000, 10000, 100000, 1000000]
    digits = map(d, j)
    answer = prod(digits)
    print (f"@ The answer for Euler #40: {answer}")
    report_timing()