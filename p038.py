# Pandigital multiples
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?

# 3 numbers - 3-digit numbers = 192384576
# 5 numbers - 1 digit + 4-2digits = 918274645
# 2 numbers - a 5 digit + a 4 digit number.

from typing import List

def is_pandigital(numbers: List[int]) -> bool:
    """
    Returns True if the list of numbers is pandigital, False otherwise.
    
    >>> is_pandigital([1,2,3,4,5])
    False
    >>> is_pandigital([12,34,56,789])
    True
    >>> is_pandigital([123,456,789])
    True
    """
    h = set()
    for n in numbers:
        for d in str(n):
            if d == '0':
                return False
            if d in h:
                return False
            else:
                h.add(d)
    if len(h) != 9:
        return False
    return True

def two_numbers() -> List[List[int]]:
    res = []
    for i in range(4999, 10**5):
        if is_pandigital([i, 2*i]):
            res.append([i, 2*i])
    return res

def three_numbers() -> List[List[int]]:
    res = []
    for i in range(111, 10**4):
        if is_pandigital([i, 2*i, 3*i]):
            res.append([i, 2*i, 3*i])
    return res

def four_numbers() -> List[List[int]]:
    res = []
    for i in range(11, 10**3):
        if is_pandigital([i, 2*i, 3*i, 4*i]):
            res.append([i, 2*i, 3*i, 4*i])
    return res

def five_numbers() -> List[List[int]]:
    res = []
    for i in range(1, 10):
        if is_pandigital([i, 2*i, 3*i, 4*i, 5*i]):
            res.append([i, 2*i, 3*i, 4*i, 5*i])
    return res

def all_numbers():
    funcs = [five_numbers, four_numbers, three_numbers, two_numbers]
    for f in funcs:
        for r in f():
            yield r

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    m, res = 0, []
    for r in all_numbers():
        n = int("".join(list(map(str, r))))
        if n > m:
            m = n
            res = r
    print("Euler Problem 38 answer:", m)
    print("The answe is composed of the following numbers:", res)