
# Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
#
#     1^2 + 2^2 + 3^2 + ... 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
#     (1 + 2 + 3 + ... 10)^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the
# square of the sum is 3025-385=2640
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
#
# Reference: https://www.cuemath.com/algebra/sum-of-squares/

def sum_of_squares(n: int) -> int:
    """
    Returns the sum of the squares of the first n natural numbers.

    >>> sum_of_squares(10)
    385
    """
    return n * (n + 1) * (2*n + 1) // 6

def square_of_sum(n: int) -> int:
    """
    Returns square of the sum of the first n natural numbers.

    >>> square_of_sum(10)
    3025
    """

    return n * (n + 1) * n * (n + 1) // 4

def sum_square_diff(n: int) -> int:
    """
    Returns the difference between square of the sum of the first n
    natural numbers and sum of the squares of those numbers.
    
    >>> sum_square_diff(10)
    2640
    
    >>> sum_square_diff(100)
    25164150
    """
    return square_of_sum(n) - sum_of_squares(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print('@ Answer to Euler #6:', sum_square_diff(100))