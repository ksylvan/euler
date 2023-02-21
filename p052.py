# Permuted multiples
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same
# digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#

from testing import report_timing, run_doctest, timer

@timer
def has_same_digits(x: int, y: int) -> bool:
    """
    Given two integers x and y, this function returns True if they have the same digits, and False otherwise.
    >>> has_same_digits(125874, 25174)
    False
    >>> has_same_digits(125874, 251748)
    True
    """
    return sorted(str(x)) == sorted(str(y))

@timer
def find_smallest_permuted_multiple() -> int:
    """
    This function finds the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
    """
    x = 1
    while True:
        if all(has_same_digits(x, i*x) for i in range(2, 7)):
            return x
        x += 1

if __name__ == '__main__':
    run_doctest()
    print("@ Euler Problem 52 answer:", find_smallest_permuted_multiple())
    report_timing()