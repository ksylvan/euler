# Maximum path sum I
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem 
# by trying every route. However, Problem 67, is the same challenge with a triangle 
# containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
#

from functools import cache
from testing import report_timing, run_doctest, timer
from typing import List

t = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],]

@timer
def max_path(triangle: List[List[int]]) -> int:
    """
    Returns the maximum total from top to bottom of the input triangle.
    
    >>> max_path([[1], [2, 3], [4, 5, 6]])
    10
    >>> max_path(t)
    1074
    """
    if not triangle:
        return 0
    @cache
    def max_it(row: int, col: int) -> int:
        n = len(triangle)
        if row < 0 or col < 0 or row >= n or col >= n:
            return 0
        if row == n-1:
            return triangle[n-1][col]
        return triangle[row][col] + max(max_it(row+1, col), max_it(row+1, col+1))
    return max_it(0, 0)

if __name__ == "__main__":
    run_doctest()
    print("@ Answer to Euler #18: ", max_path(t))
    report_timing()