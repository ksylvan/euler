# Names scores
#
# Using p022_names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

from typing import List
from functools import cache

def get_names_from_file(fname: str) -> List[str]:
    with open(fname, 'r') as f:
        names = f.read().split(',')
    for i in range(len(names)):
        names[i] = names[i].strip()
        names[i] = names[i].replace('"', '')
    return names

def name_value(s: str) -> int:
    """
    Calculate the name score for a given name.

    >>> name_value("COLIN")
    53
    """
    res = 0
    for c in s:
        res += ord(c) - ord('A') + 1
    return res

@cache
def solve() -> int:
    """
    Solve the given problem (sum of all name values multiplied by their position)

    >>> solve()
    871198282
    """
    names = get_names_from_file('p022_names.txt')
    names.sort()
    res = 0
    for i, v in enumerate(names):
        res += (i + 1)*name_value(v)
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(f'@ The answer to Euler #22 is: {solve()}')