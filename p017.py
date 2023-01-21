
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.
#
# Dictionary to store the number of letters used for each number from 1 to 19

from testing import report_timing, run_doctest, timer

@timer
def num2word(n: int) -> str:
    up_to_19 = ['one', 'two', 'three', 'four', 'five', 'six',
                'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty',
            'sixty', 'seventy', 'eighty', 'ninety']
    result = ''
    while n > 0:
        if n == 1000:
            result += 'onethousand'
            break
        elif n >= 100:
            r = n % 100
            result += up_to_19[(n//100)-1] + 'hundred'
            if r:
                result += 'and'
            n = r
        elif n >= 20:
            r = n % 10
            result += tens[(n-r)//10 - 2]
            n = r
        else:
            result += up_to_19[n-1]
            n = 0
    return result

@timer
def letters_up_to_1000() -> int:
    """
    >>> letters_up_to_1000()
    21124
    """
    res = 0
    for n in range(1, 1001):
        res += len(num2word(n))
    return res

if __name__ == '__main__':
    run_doctest()
    print('@ Answer to Euler #17:', letters_up_to_1000())
    report_timing()
