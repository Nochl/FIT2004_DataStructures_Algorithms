"""Task 1  - Enoch Leow 30600022 """

from math import pow
from math import log
from math import ceil
import random
import time


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


"""Task 2  - Enoch Leow 30600022 """

test = [random.randint(1,(2**64)-1) for _ in range(100000)]
bases = [2, 10, 604, 6483, 23749, 435434, 2135273, 4544213, 35345135, 54357893]


def time_radix_sort():
    """
    Times radix_sort function using list of random integers and bases
    :time complexity: O(1) no inputs
    :return: list of tuples containing (base, function running time in seconds)
    """
    results = []                                            # Initialise results list
    for i in bases:                                         # run radix sort using each base in list bases
        t0 = time.time()                                    # record time at start
        radix_sort(test, i)
        t1 = time.time()                                    # record time at end of function completion
        timed = t1-t0                                       # time = time start - time end
        results.append((i, timed))                          # record base used and time taken as tuple into results
    print(results)                                          # print results list


"""Task 3  - Enoch Leow 30600022 """


def find_rotations(string_list, p):
    """
    Takes list of strings and rotates each string p times to the left and returns any that appear in the original list
    :time complexity: O(NM) where
        N is the number of strings in the input list
        M is the maximum number of letters in a word, among all words in the input list
    *** radix_sort is O((N+b)M) but as b is a constant (26) it just becomes O(NM)
    :param string_list: list of unique strings made of lowercase letters
    :param p: integer representing number of rotations to the left
    :return: list of all string in string_list whose p-rotations also exist in string_list

    """
    hold = string_list.copy()                               # creates copy of list (not alter original list)
    rotated = []                                            # initialise rotated list
    for i in hold:                                          # rotate each string in list
        rotated.append(rotate(i, p))
    sorted = radix_sort_string(hold+rotated, 26)            # sort original and rotated strings into sorted
    is_rotation = []
    for i in range(1, len(sorted)):                         # adds string into is-rotation if it appears more than once
        if sorted[i] == sorted[i-1] and len(sorted) - 1:
            is_rotation.append(sorted[i])

    for i in range(len(is_rotation)):                       # un-rotates strings to give original string
        is_rotation[i] = rotate(is_rotation[i], -p)
    return is_rotation                                      # returns strings common of original & rotated lists


def rotate(string, p):
    """
    rotates sting p movements in the left direction
    :time complexity: O(1)
    :param string: string with all lowercase letters
    :param p: any integer
    :return: original string rotated p movements to the left
    """
    rotations = p%len(string)                               # calculate how many rotations
    return string[rotations:] + string[:rotations]          # return rotated string


def radix_pass_string(array, base, digit):
    """
    Sorts elements in array from smallest to largest according to specified digit and using provided base
    :time complexity: O(N+b) where
        N is the total number of strings in the input list
        b is the base
    :param array: List containing strings made of lowercase letters
    :param base: Any integer in the range [2, inf]
    :param digit: Integer representing what letter position to compute eg. 1, 2, 3...
    :return: Sorted array from smallest to largest according to specified digit
    """
    count = (base+1) * [0]                                  # Initialise count for each base value

    for i in range(len(array)):                             # Counts number of each base value
        if digit > len(array[i])-1:
            count[0] += 1
        else:
            count[ord(array[i][digit])-96] += 1
    pos = (base+1) * [0]                                    # Initialise position to store element index's
    for value in range (1, base+1):                         # Places initial index for each base value in pos
        pos[value] = pos[value-1] + count[value-1]
    temp = len(array) * [0]                                 # initialise temp list for sorted list

    for i in range(len(array)):                             # place each element from array into list
        if digit > len(array[i]) - 1:                       # assumes lowest value(0) if there is no letter in that-
            temp[pos[0]] = array[i]                         # -position
            pos[0] += 1
        else:
            num = ord(array[i][digit])-96
            temp[pos[num]] = array[i]
            pos[num]+= 1

    return temp                                             # return sorted list according to letter


def radix_sort_string(array, base):
    """
    Takes as input a list of strings to be sorted and a base, returns the sorted list (small>lar)
    :time complexity: O((N+b)M) where
        N is the total number of strings in the input list
        b is the base
        M is the number of letters in the largest string in the input list, when represented in
        base b
    :param array: List containing lowercase integers
    :param base: Any integer in the range [2, inf)
    :return: Sorted list (small>lar)
    """
    maximum = max(array)                                    # finds string with largest length in list
    temp = array.copy()                                     # creates copy of list (not modify original input)
    for i in range(len(maximum)):                           # for each letter position till max letter position
        temp = radix_pass_string(temp, base, i)             # sort strings by letter
    return temp                                             # return sorted list
