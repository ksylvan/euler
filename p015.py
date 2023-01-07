# Lattice paths
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def lattice_paths(n: int) -> int:
    """
    Use math (combinatorics) to derive the total number of lattice paths.
    
    The result is the number of possible combinations of right and down turns in a string of 2n length.
    Combination of n choose 2n = 2n! / n! which we can calculate in O(n) time and O(1) space.

    >>> lattice_paths(2)
    6
    >>> lattice_paths(3)
    20
    >>> lattice_paths(4)
    70
    >>> lattice_paths(20)
    137846528820
    
    """
    res = 1
    for i in range(1, n+1):
        res *= (n + i)
        res //= i
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print('@ Answer for Euler #15:', lattice_paths(20))