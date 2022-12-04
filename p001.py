# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples_of_3_or_5_below_n(n: int) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.
    
    >>> sum_of_multiples_of_3_or_5_below_n(10)
    23
    
    >>> sum_of_multiples_of_3_or_5_below_n(20)
    78

    >>> sum_of_multiples_of_3_or_5_below_n(1000)
    233168
    
    """
    # The sum of all multuples of 3 below n can be calculated using the following formula:
    #
    # 3 + 6 + 9 + 12 + 15 + 18 + 21 + 24 + 27 + 30 ... = 3(1+2+3+4+5+6+7+8+9+10)
    # So... 1+2+...k = 3*k(k+1)/2
    #
    # The sum of all multuples of 5 below n can be calculated using the following formula:
    # 5(1+2+3+4+5+6+7+8+9+10)
    #
    # Therefore, we divide out input n by 3 (to get the k)
    # k = n//3, then the sum of the 3-multiples = k*(k+1)/2
    # Similarly, we divide out input n by 5 (to get the k)
    # k = n//5, then the sum of the 5-multiples = 5*k*(k+1)/2
    #
    # The only problem is that we have double-counted any number
    # that is a mltiple of 3 AND 5. So subtracting that will give
    # the sum of all the multiples of 3 or 5 below n.
    #

    # Calculate the sum of all the multiples of 3 below n
    k = (n - 1) // 3
    s = 3 * k * (k + 1) // 2

    # Calculate the sum of all the multiples of 5 below n
    k = (n - 1) // 5
    s += 5 * k * (k + 1) // 2
    
    # Calculate the sum of all the multiples of 15 below n
    k = (n - 1) // 15
    s -= 15 * k * (k + 1) // 2
    
    return s

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)