# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# January 1st 1900 was a Monday.
#

from datetime import date

from testing import report_timing, run_doctest, timer

@timer
def answer() -> int:
    """
    Return the number of Sundays that ended up as the first day of the month
    between 1/1/1901 and 12/31/2000.
    
    >>> answer()
    171
    """
    
    res = 0
    for y in range(1901, 2001):
        for m in range(1, 13):
            d = date(y, m, 1)
            if d.weekday() == 6:
                res += 1
    return res

if __name__ == "__main__":
    run_doctest()
    print("@ Answer to Euler #19 (Sundays on 1st of the month in 20th century):", answer())
    report_timing()