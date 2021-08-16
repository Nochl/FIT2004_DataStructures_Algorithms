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
    hold = string_list.copy()                                       # creates copy of list (not alter original list)
    rotated = []                                                    # initialise rotated list
    for i in hold:                                                  # rotate each string in list
        rotated.append(rotate(i, p))
    sorted = radix_sort(hold+rotated, 26)                           # sort original and rotated strings into sorted
    isrotation = []
    for i in range(1, len(sorted)):                                 # adds string into isrotation if it appears more-
        if sorted[i] == sorted[i-1] and len(sorted) -1:             # -than once
            isrotation.append(sorted[i])

    for i in range(len(isrotation)):                                # unrotates strings to give original string
        isrotation[i] = rotate(isrotation[i], -p)
    return isrotation                                               # returns strings common of original & rotated lists


def rotate(string, p):
    """
    rotates sting p movements in the left direction
    :time complexity: O(1)
    :param string: string with all lowercase letters
    :param p: any integer
    :return: original string rotated p movements to the left
    """
    rotations = p%len(string)                                       # calculate how many rotations
    return string[rotations:] + string[:rotations]                  # return rotated string


def radix_pass(array, base, digit):
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
    count = (base+1) * [0]                                          # Initialise count for each base value

    for i in range(len(array)):                                     # Counts number of each base value
        if digit > len(array[i])-1:
            count[0] += 1
        else:
            count[ord(array[i][digit])-96] += 1
    pos = (base+1) * [0]                                            # Initialise position to store element index's
    for value in range (1, base+1):                                 # Places initial index for each base value in pos
        pos[value] = pos[value-1] + count[value-1]
    temp = len(array) * [0]                                         # initialise temp list for sorted list

    for i in range(len(array)):                                     # place each element from array into list
        if digit > len(array[i]) - 1:                               # assumes lowest value(0) if there is no letter in-
            temp[pos[0]] = array[i]                                 # -that position
            pos[0] += 1
        else:
            num = ord(array[i][digit])-96
            temp[pos[num]] = array[i]
            pos[num]+= 1

    return temp                                                     # return sorted list according to letter


def radix_sort(array, base):
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
    maximum = max(array)                                            # finds string with largest length in list
    temp = array.copy()                                             # creates copy of list (not modify original input)
    for i in range(len(maximum)):                                   # for each letter position till max letter position
        temp = radix_pass(temp, base, i)                            # sort strings by letter
    return temp                                                     # return sorted list
