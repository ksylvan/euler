# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?

from collections import defaultdict
from math import sqrt
from typing import Dict

from testing import report_timing, run_doctest, timer

class Solution:
    @timer
    def factors(self, n: int) -> Dict[int, int]:
        d = defaultdict(int)
        while n % 2 == 0:
            d[2] += 1
            n //= 2
        for p in range(3, int(sqrt(n)) + 1, 2):
            while n % p == 0:
                d[p] += 1
                n //= p
        if n > 1:
            d[n] += 1
        return d
    
    @timer
    def smallestMultiple(self, n: int) -> int:
        """
        >>> Solution().smallestMultiple(10)
        2520
        
        >>> Solution().smallestMultiple(20)
        232792560
        """
        if n <= 1:
            return 1
        final_factors = self.factors(2)
        for i in range(3, n+1):
            d = self.factors(i)
            for k, v in d.items():
                final_factors[k] = max(final_factors.get(k, 0), v)
        res = 1
        for k, v in final_factors.items():
            res *= pow(k, v)
        return res

if __name__ == "__main__":
    run_doctest()
    print('@ Answer to Euler #5:', Solution().smallestMultiple(20))
    report_timing()