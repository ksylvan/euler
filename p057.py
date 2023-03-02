# Square root convergents
#
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# sqrt(2) = 1 + 1
#              ______________
#               2 + 1
#                   ______________
#                   2 + 1 [...]
#
# By expanding this for the first four iterations, we get:
#
# 1: 1 + 1/2 = 1.5 = 3/2
# 2: 1 + 1/(2+1/2) = 1+ 1/(5/2) = 1+ 2/5 = 7/5
# 3: 17/12
# 4: 41/29
# 5: 99/70
# 6: 239/169
# 7: 577/408
#
# But the 8th is 1393/585 the first example where the number of digits in
# the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a
# numerator with more digits than the denominator?

from testing import run_doctest, report_timing, timer

@timer
def continued_fraction_sqrt2():
    """Yield the numerator and denominator of each fraction in the continued fraction series for sqrt(2).
    
    >>> f = continued_fraction_sqrt2()
    >>> next(f)
    (3, 2)
    >>> next(f)
    (7, 5)
    >>> next(f)
    (17, 12)
    >>> next(f)
    (41, 29)
    >>> next(f)
    (99, 70)
    """
    # Initialize the first two fractions
    p, q = 1, 1
    
    # Iterate to the n-th fraction
    while True:
        # Compute the next numerator and denominator
        p, q = 2 * q + p, p + q
        
        # Yield the next fraction
        yield p, q

@timer 
def ans(n: int) -> int:
    """count how many of the first n continued fraction have a numerator with more digits than the denominator.
    
    >>> ans(10)
    1
    """
    f = continued_fraction_sqrt2()
    count = 0
    for _ in range(n):
        p, q = next(f)
        if len(str(p)) > len(str(q)):
            count += 1
    return count

if __name__ == "__main__":
    run_doctest()
    res = ans(1000)
    print("@ Euler #57 answer is: ", res)
    report_timing()