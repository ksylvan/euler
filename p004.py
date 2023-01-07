# Largest palindrome product

# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from math import sqrt
from typing import List
from heapq import heappop, heapify

class Solution:
    """
    Return the prime factors of n.
    
    >>> Solution().factors(70)
    [2, 5, 7]
    >>> Solution().factors(13)
    [13]
    >>> Solution().factors(169)
    [13, 13]
    """
    def factors(self, n: int) -> List[int]:
        result = []
        while n % 2 == 0:
            result.append(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                result.append(i)
                n //= i
        if n > 1:
            result.append(n)
        return result
    
    def isPalindromicNumber(self, n: int) -> bool:
        """
        True if the input is a palindromic integer.
        
        >>> Solution().isPalindromicNumber(91)
        False
        >>> Solution().isPalindromicNumber(1001)
        True
        >>> Solution().isPalindromicNumber(76567)
        True
        """
        if n < 0:
            res = False
        elif n == 0:
            res = True
        else:
            digits = []
            while n!= 0:
                digits.append(n % 10)
                n //= 10
            k = len(digits)
            res = True
            for i in range(k//2 + 1):
                if digits[i]!=digits[-(i+1)]:
                    res = False
                    break        
        return res
    
    def largestPalindrome(self, n: int) -> int:
        """
        Return the largest palindrome made by multiiplying two n-digit numbers.
        
        >>> Solution().largestPalindrome(2)
        9009
        >>> Solution().largestPalindrome(3)
        906609
        """
        s = set()
        k = pow(10, n) - 1
        l = int("1"*n)
        for i in range(k, l-1, -1):
            for j in range(k, l-1, -1):
                s.add(-i*j)
        h = list(s)
        heapify(h)
        while h:
            res = -heappop(h)
            if self.isPalindromicNumber(res):
                return res
        return -1
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print('@ Answer to Euler #4:', Solution().largestPalindrome(3))
