# decorators and utility methods used for testing

from collections import defaultdict
from functools import cache, wraps
from os import environ, path
from time import time

def timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        global timings
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        if 'timings' not in globals():
            timings = defaultdict(float)
        timings[f"{func.__name__}"] += (end_time - start_time)
        return result
    return wrapper

def run_doctest() -> None:
    if environ.get("TESTING"):
        import doctest
        doctest.testmod(verbose=True)
    
def report_timing() -> None:
    if environ.get("TIMING"):
        global timings
        print("Timings:")
        if 'timings' in globals():
            for f in timings:
                print(f"    {f}: {timings[f]}")
        else:
            print("Warning: No timing data found.")

@timer
def fib(n: int) -> int:
    """
    Return fibonacci numbers.
    
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

@cache
@timer
def cached_fib(n: int) -> int:
    """
    Return fibonacci numbers.
    
    >>> cached_fib(0)
    0
    >>> cached_fib(1)
    1
    >>> cached_fib(2)
    1
    >>> cached_fib(3)
    2
    >>> cached_fib(4)
    3
    >>> cached_fib(5)
    5
    >>> cached_fib(6)
    8
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return cached_fib(n - 1) + cached_fib(n - 2)

@timer
def simple_test():
    """
    This main function will simply demo doctests.
    
    >>> simple_test()
    1234
    
    """
    x = fib(25)
    y = cached_fib(25)
    return 1234

if __name__ == "__main__":
    run_doctest()
    _ = simple_test()
    print(f"@ This utility module ({path.basename(__file__)}) does not answer any Euler project questions.")
    report_timing()