# Lychrel numbers
#
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never
# produce a palindrome. A number that never forms a palindrome through the reverse and 
# add process is called a Lychrel number. Due to the theoretical nature of these numbers, 
# and for the purpose of this problem, we shall assume that a number is Lychrel until proven
# otherwise. In addition you are given that for every number below ten-thousand, 
# it will either (i) become a palindrome in less than fifty iterations, or, 
# (ii) no one, with all the computing power that exists, has managed so far to map 
# it to a palindrome. In fact, 10677 is the first number to be shown to require over 
# fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical 
# nature of Lychrel numbers.

from testing import report_timing, run_doctest, timer

def is_palindrome(n: int) -> bool:
    """Return True if n is a palindrome, False otherwise.
    
    >>> is_palindrome(121)
    True
    >>> is_palindrome(4213)
    False
    >>> is_palindrome(7337)
    True
    """
    return str(n) == str(n)[::-1]

@timer
def is_lychrel(n: int, max_iterations: int = 50) -> bool:
    """Return True if n is a Lychrel number, False otherwise.
    
    >>> is_lychrel(121)
    False
    >>> is_lychrel(4213)
    False
    >>> is_lychrel(196)
    True
    """
    for i in range(max_iterations):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True

@timer
def lychrel_numbers(below_number: int) -> int:
    count = 0
    for i in range(1, below_number):
        if is_lychrel(i):
            count += 1
    return count

if __name__ == '__main__':
    run_doctest()
    ans = lychrel_numbers(10000)
    print("@ Euler #55 answer:", ans)
    report_timing()