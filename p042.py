# Coded triangle numbers
#
# The nth term of the sequence of triangle numbers is given by, t(n) = 1/2*n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding
# these values we form a word value.
# 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number
# then we shall call the word a triangle word.
#
# How many triangle words are there in the words.txt file?
#

# We need to solve for: N = (x)(x+1)/2, or x^2 + x -2N = 0
# This solves (via the quadratic equation) to:
# x = (-1 +- sqrt(1 +8N))/2

from typing import List
from math import sqrt

def get_words_from_file(fname: str) -> List[str]:
    with open(fname, 'r') as f:
        words = f.read().split(',')
    for i in range(len(words)):
        words[i] = words[i].strip()
        words[i] = words[i].replace('"', '')
    return words

def is_triangle_word(word: str) -> bool:
    """
    Return True if the word is a triangle word, False otherwise.
    
    >>> is_triangle_word('SKY')
    True
    >>> is_triangle_word('ABD')
    False
    """
    alphabet_to_number = {char: ord(char) - ord('a') + 1 for char in 'abcdefghijklmnopqrstuvwxyz'}
    w = word.lower()
    n = sum([alphabet_to_number[c] for c in w])
    x = (-1 + sqrt(1 + 8*n))/2
    return x == int(x)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    words = get_words_from_file('p042_words.txt')
    n = 0
    for word in words:
        if is_triangle_word(word):
            n += 1
    print(f"@ Answer for Euler #42: {n}")                
