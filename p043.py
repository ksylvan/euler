# Sub-string divisibility
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each
# of the digits 0 to 9 in some order, but it also has a rather interesting sub-string
# divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

# We'll generate all the permutations of 9-digit pandigital numbers,
# testing each substring along the way.

from functools import reduce
from itertools import permutations
from typing import Tuple

from testing import report_timing, run_doctest, timer

class PandigitalGenerator:
    """
    A class to represent a pandigital generator of all pandigital numbers of n digits.

    >>> p = PandigitalGenerator(3)
    >>> for i in p: print(i)
    12
    21
    102
    120
    201
    210
    
    We can use a filter function to vet the generated numbers.
    
    >>> p = PandigitalGenerator(3, lambda p: p[-1]%2 == 1 and p[0] != 0)
    >>> for i in p: print(i)
    201
    """
    
    @timer
    def __init__(self, n: int, filter = None):
        self.digits = range(n)
        self.filter = filter
        self._p = permutations(self.digits)

    @timer
    def __iter__(self):
        return self

    @timer
    def __next__(self):
        """
        Return the next pandigital number of the desired length.

        If filter was specified at construction, only return numbers that pass the filter.
        """
        filter = self.filter
        while True:
            x = next(self._p)
            if filter is not None:
                if not filter(x):
                    continue
            break
        return reduce(lambda a, b: 10*a+b, x)

    @timer
    def __repr__(self):
        return f"{self.__class__.__name__}({self.digits, self.filter})"

@timer
def divisibilityTest(l: Tuple[int, int, int, int, int, int, int, int, int, int]) -> bool:
    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = l
    # d2d3d4=406 is divisible by 2
    if d4%2 != 0:
        return False
    # d3d4d5=063 is divisible by 3
    if (d3 + d4 + d5)%3 != 0:
        return False
    # d4d5d6=635 is divisible by 5
    if d6%5 != 0:
        return False
    # d5d6d7=357 is divisible by 7
    if (2*d5 + 3*d6 + d7)%7 != 0:
        return False
    # d6d7d8=572 is divisible by 11
    if (d6+10*d7+d8)%11 != 0:
        return False
    # d7d8d9=728 is divisible by 13
    if (9*d7 + 10*d8 + d9) %13 != 0:
        return False
    # d8d9d10=289 is divisible by 17
    if (15*d8 + 10*d9 + d10) %17!= 0:
        return False
    return True
    
if __name__ == "__main__":
    run_doctest()
    p = PandigitalGenerator(10, divisibilityTest)
    numbers = []
    for i in p:
        numbers.append(i)
    print("@ Euler #43 answer:", sum(numbers))
    print("@ The list of numbers is:", numbers)
    report_timing()