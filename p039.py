# Integer right triangles
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

# Using this formula from a paper published in AIMS Mathematics
# "A new approach to generate all Pythagorean triples"
# by Anthony Overmars, Lorenzo Ntogramatzidis, Sitalakshmi Venkatraman 
# https://www.aimspress.com/article/id/3488 
#

from typing import List, Tuple
from collections import defaultdict
from itertools import count

def p(m: int, n: int) -> Tuple[int, int, int]:
    """
    Implements the generator function in the Pythagorean triples paper.
    
    Returns the tuple with the 3 integers {a, b, c}.
    
    >>> p(1, 1)
    (3, 4, 5)
    >>> p(1, 2)
    (5, 12, 13)
    """
    a = 4*m*n - 2*n + 4*m*m - 4*m + 1
    b = 2*n*n + 4*m*n - 2*n
    c = 2*n*n + 4*m*n - 2*n + 4*m*m - 4*m + 1
    return (a, b, c)

def all_pythagorean_triples():
    """
    Generator using the p(m, n) formulation.
    Yields each triple in the following order:
    p(1, 1), p(1,2), p(2, 1), p(1, 3), p(2, 2), p(3, 1), p(1, 4), p(2, 3), p(3, 2), p(4, 1), ...

    >>> g = all_pythagorean_triples()
    >>> next(g)
    (3, 4, 5)
    >>> next(g)
    (5, 12, 13)
    >>> next(g)
    (15, 8, 17)
    """
    for i in count(start = 1):
        m, n = 0, i
        while m < i:
            m += 1
            yield p(m, n)
            n -= 1
                
perimeters = defaultdict(set)
perimeter_with_most_triples = 0
most_triples_list_len = 0

def pyth_scan_to_perim(n: int) -> None:
    """
    Set up perimeters hash for up to perimeter <= n.
    """
    global perimeters, perimeter_with_most_triples, most_triples_list_len
    g = all_pythagorean_triples()
    for p in g:
        for c in count(1):
            perim = sum(p)
            if c * perim > n:
                break
            l = tuple(map(lambda x: c * x, p))
            perimeters[c*perim].add(l)
            if len(perimeters[c*perim]) > most_triples_list_len:
                most_triples_list_len = len(perimeters[c*perim])
                perimeter_with_most_triples = c * perim
        if perim > n:
            break

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    pyth_scan_to_perim(1000)
    print(f"@ Answer to Euler 39: perimeter_with_most_triples = {perimeter_with_most_triples}")
    print(f"@ That perimeter is reached with {most_triples_list_len} triples")
    print(f"@ The list of Pythagorean Triples with that parameter: {perimeters[perimeter_with_most_triples]}")
