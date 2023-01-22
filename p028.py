# Number spiral diagonals
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
# is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from testing import report_timing, run_doctest, timer

@timer
def spiralDiagSum(n: int) -> int:
    """
    O(1) solution for the spiral diagonal sum problem.
    
    >>> spiralDiagSum(1)
    1
    >>> spiralDiagSum(3)
    25
    >>> spiralDiagSum(5)
    101
    >>> spiralDiagSum(101)
    692101
    >>> spiralDiagSum(1001)
    669171001
    """

    if n & 1:
        return (4*n**3 + 3*n**2 + 8*n - 9) // 6
    else:
        raise ValueError("square side should be odd.", n)


if __name__ == "__main__":
    run_doctest()
    print(f"@ The answer to Euler 28 is: {spiralDiagSum(1001)}")
    report_timing()