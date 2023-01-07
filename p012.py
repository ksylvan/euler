# Highly divisible triangular number
#
# The nth triangle number is n * (n + 1)
#
# https://en.wikipedia.org/wiki/Triangular_number
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the first triangle number to have over five hundred divisors?
#
# Code was mostly written by ChatGPT https://chat.openai.com/chat

from typing import List, Dict

def extend_primeas(primes: List[int], v: int) -> None:
    last_prime = primes[-1]
    while last_prime * last_prime < v:
        while True:
            next_prime = last_prime + 2
            is_prime = True
            for p in primes:
                if p * p > next_prime:
                    break
                if next_prime % p == 0:
                    is_prime = False
                    last_prime += 2
                    break
            if is_prime:
                primes.append(next_prime)
                last_prime = next_prime
                break

def factorize(n: int, primes: List[int], prime_factors: Dict[int,int]) -> None:
    # Loop over all primes
    for p in primes:
        # Counter for the current prime
        count = 0

        # While n is divisible by p, increment the counter, add p to the
        # dictionary of prime factors, and divide n by p
        while n % p == 0:
            count += 1
            prime_factors[p] = count
            n //= p

    # Return the dictionary of prime factors and their powers
    return prime_factors

def first_triangle_number_with_over_n_divisors(n: int) -> int:
    """
    >>> first_triangle_number_with_over_n_divisors(5)
    28
    
    >>> first_triangle_number_with_over_n_divisors(10)
    120
    
    >>> first_triangle_number_with_over_n_divisors(20)
    630
    
    >>> first_triangle_number_with_over_n_divisors(50)
    25200
    
    >>> first_triangle_number_with_over_n_divisors(500)
    76576500
    """
    # Initialize the triangle number to 1
    triangle_number = 1

    # Initialize the list of primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Iterate over the triangle numbers
    for i in range(2, 100000000):
        # Calculate the next triangle number
        triangle_number += i

        # extend the primes list if needed
        extend_primeas(primes, triangle_number)

        # prime_factorization of the triangle number
        prime_factorization = {}
        factorize(triangle_number, primes, prime_factorization)
        
        # Calculate the number of divisors of the triangle number
        divisors = 1
        for exp in prime_factorization.values():
            divisors *= (exp + 1)

        # If the number of divisors is greater than 500, return the triangle number
        if divisors > n:
            return triangle_number

    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print('@ Answer to Euler #12:', first_triangle_number_with_over_n_divisors(500))
