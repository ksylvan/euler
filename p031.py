# Coin sums
#
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#

from functools import cache
from typing import List

from testing import report_timing, run_doctest, timer


class CoinChange:
    @timer
    def __init__(self, coins: List[int]) -> None:
        "Constructor for CoinChange object. Store the list of coin denominations."
        self.coins = sorted(coins)

    @timer
    @cache
    def waysToMakeChange(self, amount: int) -> int:
        """
        Returns the number of ways to make change for n, given the list of denominations.
        This Dynamic Programming solution was written by GPT-3.

        >>> CoinChange([1]).waysToMakeChange(1)
        1
        >>> CoinChange([1, 2]).waysToMakeChange(2)
        2
        >>> CoinChange([1, 2]).waysToMakeChange(3)
        2
        >>> c = CoinChange([1,2,5,10,20,50,100,200])
        >>> c.waysToMakeChange(200)
        73682
        """
        # Initialize the array of ways to make change
        ways = [0] * (amount + 1)
        # There is only one way to make 0 cents (using no coins)
        ways[0] = 1
        
        # Loop through each coin denomination
        for c in self.coins:
            # Loop through the ways array starting at index c
            for i in range(c, amount+1):
                # Increment the number of ways to make change at index i
                # by the number of ways to make change at index i - c
                ways[i] += ways[i - c]
        
        # Return the number of ways to make change for N
        return ways[amount]

if __name__ == '__main__':
    run_doctest()
    c = CoinChange([1,2,5,10,20,50,100, 200])
    print(f"@ Euler problem 31 answer is: {c.waysToMakeChange(200)}")
    report_timing()