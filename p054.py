# In the card game poker, a hand consists of five cards and are ranked, 
# from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives 
# (see example 1 below). But if two ranks tie, for example, both players have 
# a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.

# For example, consider the following hands:
# Hand	 	Player 1	 	Player 2	 	Winner
#       5H 5C 6S 7S KD   2C 3S 8S 8D TD     Player 2
#       (Pair of 5s)     (Pair of 8s)

# The file, p054_poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): 
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards), 
# each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

from collections import Counter
from typing import List, Tuple

from testing import report_timing, run_doctest, timer

@timer
def rank(hand: List[Tuple[int, str]]) -> Tuple[int, Tuple[int, int, int, int, int]]:
    """
    Given a poker hand, returns a tuple with an integer as the first value (representing the rank of the hand) 
    and a tuple as the second value. This tuple contains all the values of the cards in the hand, but is arranged 
    differently for each kind of hand (see below for details).
    
    >>> rank([(5, 'S'), (3, 'C'), (3, 'S'), (5, 'D'), (12, 'D')])
    (2, (5, 3, 12))
    >>> rank([(5, 'S'), (3, 'C'), (3, 'S'), (5, 'D'), (5, 'D')])
    (6, (5, 3))
    >>> rank([(3, 'H'), (3, 'C'), (3, 'S'), (5, 'C'), (5, 'D')])
    (6, (3, 5))
    """

    # Sort the hand by value
    sorted_hand = sorted(hand, key=lambda x: x[0], reverse=True)

    # Get the set of values and suits
    values = [card[0] for card in sorted_hand]
    suits = set([card[1] for card in sorted_hand])

    # Royal Flush
    if len(suits) == 1 and values == [14, 13, 12, 11, 10]:
        return (9, tuple(values))

    # Straight Flush
    if len(suits) == 1 and values == list(range(values[0], values[0]-5, -1)):
        return (8, tuple(values))

    # Four of a Kind
    if len(set(values)) == 2:
        for value in set(values):
            if values.count(value) == 4:
                return (7, (value, [v for v in values if v != value][0]))
    
    # Full House
    if len(set(values)) == 2:
        for value in set(values):
            if values.count(value) == 3:
                return (6, (value, [v for v in values if v != value][0]))

    # Flush
    if len(suits) == 1:
        return (5, tuple(values))

    # Straight
    if values == list(range(values[0], values[0]-5, -1)):
        return (4, tuple(values))

    # Three of a Kind
    if len(set(values)) == 3:
        for value in set(values):
            if values.count(value) == 3:
                return (3, (value, [v for v in values if v != value][::-1]))

    # Two Pairs
    if len(set(values)) == 3:
        pairs = [value for value in set(values) if values.count(value) == 2]
        if len(pairs) == 2:
            pairs.sort(reverse=True)
            return (2, tuple(pairs + [value for value in values if value not in pairs][::-1]))

    # One Pair
    if len(set(values)) == 4:
        for value in set(values):
            if values.count(value) == 2:
                return (1, tuple([value] + sorted([v for v in values if v != value][::-1], reverse=True)))

    # High Card
    return (0, tuple(values))

@timer
def compare(hands:List[List[Tuple[int, str]]]) -> int:
    """
    Given a list of two poker hands, returns the index (0 or 1) of the winning hand, or -1 if the hands tie.
    The winning hand is determined according to the rules of poker, with higher-ranked hands beating lower-ranked ones.
    In case of a tie, the highest card value is used to break the tie, and if that is also tied, the next highest value is used, and so on.

    >>> compare([[(8, 'C'), (10, 'S'), (13, 'C'), (9, 'H'), (4, 'S')], [(7, 'D'), (2, 'S'), (5, 'D'), (3, 'S'), (14, 'C')]])
    1
    """
    if not hands or len(hands) != 2 or len(hands[0]) != 5 or len(hands[1]) != 5:
        return -1

    rank1 = rank(hands[0])
    rank2 = rank(hands[1])

    if rank1 > rank2:
        return 0
    elif rank1 < rank2:
        return 1
    else:
        # Tie
        return -1

@timer
def read_hands(filename: str):
    """
    Given a filename, reads a list of poker hands from the file and yields them as pairs of hands.
    Each hand is represented as a list of pairs (value, suit), with the first five cards belonging to Player 1 and the last five cards belonging to Player 2.
    """
    with open(filename) as f:
        for line in f:
            cards = line.strip().split()
            hand1 = [(parse_value(v), s) for v, s in cards[:5]]
            hand2 = [(parse_value(v), s) for v, s in cards[5:]]
            yield hand1, hand2

@timer
def parse_value(value: str) -> int:
    """
    Given a string representation of a card value (e.g., 'A', 'K', 'Q', 'J', 'T', or a number), returns its integer value (2-14).
    
    >>> parse_value('A')
    14
    >>> parse_value('K')
    13
    """
    if value == 'A':
        return 14
    elif value == 'K':
        return 13
    elif value == 'Q':
        return 12
    elif value == 'J':
        return 11
    elif value == 'T':
        return 10
    else:
        return int(value)

@timer
def answer() -> int:
    filename = 'p054_poker.txt'
    count = 0
    for hand1, hand2 in read_hands(filename):
        if compare([hand1, hand2]) == 0:
            count += 1
    return count

if __name__ == '__main__':
    run_doctest()
    ans = answer()
    print("@ Euuler #54 answer is:", ans)
    report_timing()