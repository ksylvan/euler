# Double-base palindromes
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
#

from typing import List

def isPalindrome(s: str) -> bool:
    """
    Return True if the string is a palindrome, else False.
    
    >>> isPalindrome('ab')
    False
    >>> isPalindrome('abcba')
    True
    >>> isPalindrome('')
    True
    """
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def binPalindrome(n: int) -> bool:
    """
    Return True if the number is a palindrome in binary, else False.
    
    >>> binPalindrome(585)
    True
    >>> binPalindrome(586)
    False
    """
    return isPalindrome(bin(n)[2:])    

def decimalPalindromesLessThan(n: int) -> int:
    """
    Generator of decimal palindromes less than the given number.
    """
    def single(): # single digit palindrome
        for v in range(1, 10):
            yield v
    def double(leadingZero = False): # double digit palindrome
        if leadingZero:
            yield 0
        for v in [k*11 for k in range(1, 10)]:
            yield v
    def triple(leadingZero = False): # triple digit palindrome
        start_with = 0 if leadingZero else 1
        for i in range(start_with, 10):
            for j in range(10):
                yield 100*i + 10*j + i
    def quadruple(leadingZero = False): # quadruple digit palindrome
        start_with = 0 if leadingZero else 1
        for i in range(start_with, 10):
            for j in range(10):
                yield 1000*i + 100*j + 10*j + i

    # single digit
    for i in single():
        if i < n:
            yield i
    # double digits
    for i in double():
        if i < n:
            yield i
    # triple digits
    for i in triple():
        if i < n:
            yield i
    # quadruple digits
    for i in quadruple():
        if i < n:
            yield i
    # 5 digits
    for i in range(1, 10):
        for j in triple(leadingZero=True):
            v = i*10000+ 10*j + i
            if v < n:
                yield v
    # 6 digits
    for i in range(1, 10):
        for j in quadruple(leadingZero=True):
            v = i*100000+ 10*j + i
            if v < n:
                yield v

def doubleBasePalindromesLessThan(n: int) -> List[int]:
    """
    Return the list of double base palindromes less than the given number.
    
    >>> doubleBasePalindromesLessThan(10)
    [1, 3, 5, 7, 9]
    >>> doubleBasePalindromesLessThan(1000)
    [1, 3, 5, 7, 9, 33, 99, 313, 585, 717]
    """
    res = []
    g = decimalPalindromesLessThan(n) # generate all decimal palindromic numbers less than n
    for i in g:
        if binPalindrome(i):
            res.append(i)
    return res
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    l = doubleBasePalindromesLessThan(1000000)
    print(f"@ Euler problem 36 answer for sum of double base palindromes less than 1000000: {sum(l)}")
    print(f"@ The numbers are: {l}")