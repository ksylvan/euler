# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
#
# 3^2 + 4^2 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Since a+b+c = 1000, and a^2 + b^2 = c^2
# c = 1000 - (a+b)
#
# Brute force, we can test the o(n^2) possible triplets:
#

from typing import List

from testing import report_timing, run_doctest, timer

@timer
def find_triplets_summing_to(n: int) -> List[List[int]]:
    """
    >>> find_triplets_summing_to(12)
    [[3, 4, 5]]
    >>> find_triplets_summing_to(2)
    []
    >>> find_triplets_summing_to(3)
    []
    >>> find_triplets_summing_to(1000)
    [[200, 375, 425]]
    """
    res = []
    if n > 5:
        for b in range(1, n-2):
            for a in range(2, b):
                c = n - a - b
                if a*a+b*b==c*c:
                    res.append([a, b, c])
    return res

if __name__ == "__main__":
    run_doctest()
    res = find_triplets_summing_to(1000)[0]
    print("@ Euler Problem 9 answer:", res[0]*res[1]*res[2])
    report_timing()