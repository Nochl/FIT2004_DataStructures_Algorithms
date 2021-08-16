"""Task 1  - Enoch Leow 30600022 """

from math import pow
from math import log
from math import ceil


def get_digit(integer, base, digit):
    """
    Get_digit computes the value of the specified 'digit' in 'base' of the 'integer'
    :time complexity: O(1)
    :param integer: Any positive integer in range [1, 2^64 − 1]
    :param base: Any integer in the range [2, inf)
    :param digit: Integer representing what digit to compute eg. 1, 2, 3...
    :return: value of the specified 'digit' in 'base' of the 'integer'
    """
    modulo = integer%pow(base, digit)                       # integer modulo(base^digit)
    modulo = modulo/pow(base, digit-1)                      # divide by base, digit-1 to isolate specified digit
    return int(modulo//1)                                   # return value in the 1s place


def radix_pass(array, base, digit):
    """
    Sorts elements in array from smallest to largest according to specified digit and using provided base
    :time complexity: O(N+b) where
        N is the total number of integers in the input list
        b is the base
    :param array: List containing positive integers in the range[1, 2^64 − 1]
    :param base: Any integer in the range [2, inf
    :param digit: Integer representing what digit to compute eg. 1, 2, 3...
    :return: Sorted array from smallest to largest according to specified digit
    """
    count = (base+1) * [0]                                  # Initialise count for each base value

    for i in range(len(array)):                             # Counts number of each base value
        count[get_digit(array[i], base, digit)] += 1
    pos = (base+1) * [0]                                    # Initialise position to store element index's
    for value in range (1, base+1):                         # Places initial index for each base value in pos
        pos[value] = pos[value-1] + count[value-1]
    temp = len(array) * [0]                                 # initialise temp list for sorted list

    for i in range(len(array)):                             # place each element from array into list according to-
        num = get_digit(array[i], base, digit)              # -index in pos
        temp[pos[num]] = array[i]
        pos[num]+= 1

    return temp                                             # return sorted list according to digit


def radix_sort(array, base):
    """
    Takes as input a list of numbers to be sorted and a base, returns the sorted list (small>lar)
    :time complexity: O((N+b)M) where
        N is the total number of integers in the input list
        b is the base
        M is the number of digits in the largest number in the input list, when represented in
        base b
    :param array: List containing positive integers in the range[1, 2^64 − 1]
    :param base: Any integer in the range [2, inf)
    :return: Sorted list (small>lar)
    """
    maximum = max(array)                                    # Maximum = max element in list
    digits = ceil(log(maximum, base)) + 1                   # calculates maximum digit of largest element +1(edge case)
    temp = array.copy()                                     # copy given array (to not modify given list)
    for i in range(1, digits+1):
        temp = radix_pass(temp, base, i)
    return temp                                             # return sorted list
