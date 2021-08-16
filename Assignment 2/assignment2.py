"""Enoch Leow 30600022"""

"""Task 1 - Oscillations"""


def longest_oscillation(L):
    """
    Find the longest oscillation in a given list L
    :time_complexity: O(N^2) - Sub-optimal
    :auxiliary_space: O(N)   - Optimal
        where N is length of given list L
    :param L: A list of integers which can contain duplicates or be empty
    :return: tuple (length of longest oscillation, [indices which make up oscillation])
    """
    maxlen = [0] * len(L)                                                  # Initialise D.P var to store len of osc
    maxlen[0] = (1, 1)

    for i in range(1, len(L)):                                             # for each element, check if larger/smaller-
        smallmax = 0                                                       # - than those before it and use D.P var to
        largemax = 0                                                       # - calculate longest len
        for j in range(0, i):

            if L[i] < L[j]:                                                # check if larger
                temp = maxlen[j][1] + 1
                if temp > smallmax:
                    smallmax = temp
                if maxlen[j][1] > largemax:
                    largemax = maxlen[j][1]

            if L[i] > L[j]:                                                # check if smaller
                temp = maxlen[j][0] + 1
                if temp > largemax:
                    largemax = temp
                if maxlen[j][0] > smallmax:
                    smallmax = maxlen[j][0]

            else:
                if maxlen[j][1] > largemax:
                    largemax = maxlen[j][1]
                if maxlen[j][0] > smallmax:
                    smallmax = maxlen[j][0]

        maxlen[i] = (smallmax, largemax)                                   # sets longest len in to D.P var

    long_osc = []                                                          # initialise backtracking vars
    count = 0
    exclude = 0

    for i in range(len(maxlen)-1):                                         # look for previous path starting from end
        if max(maxlen[i][0], maxlen[i][1]) == (max(maxlen[i+1][0], maxlen[i+1][1])-1):
            long_osc.append(i)
            count += 1
            exclude = 0

        elif L[i] == L[1+1]:
            if exclude == 0:
                long_osc.append(i)
                count += 1
                exclude = 1

        elif i == len(maxlen) - 2:
            long_osc.append(i)
            count += 1
            exclude = 1
        else:
            exclude = 1

    if exclude == 0:
        long_osc.append(len(maxlen)-1)
        count += 1

    return count, long_osc                                                 # return tuple (len osc, [path indices])


"""Task 2 - Increasing walk"""


def longpath(i, j, M, rows, columns, len_walk):
    """
    Finds the longest walk beginning from M[i][j]
    :time_complexity: O(nm) - (longest possible complexity)
    :auxiliary_space: O(nm)
        where n is rows and m is columns in matrix M
    :param i: row of M
    :param j: column of M
    :param M: Matrix to look for walk
    :param rows: number of rows in M
    :param columns: number of columns in M
    :param len_walk: D.P variable storing longest path for each cell in matrix M
    :return: longest walk beginning from M[i][j]
    """
    if i < 0 or i >= rows or j < 0 or j >= columns:                        # Base case if we check outside matrix
        return 0

    if len_walk[i][j] != -1:                                               # return stored D.P result if available
        return len_walk[i][j]

    up, down, left, right, l_up, r_up, l_down, r_down = -1, -1, -1, -1, -1, -1, -1, -1  # initialise direction var

    if i > 0 and M[i][j] < M[i - 1][j]:                                    # checks each direction for longest walk
        up = longpath(i - 1, j, M, rows, columns, len_walk) + 1

    if i < rows - 1 and M[i][j] < M[i + 1][j]:
        down = longpath(i + 1, j, M, rows, columns, len_walk) + 1

    if j > 0 and M[i][j] < M[i][j - 1]:
        left = longpath(i, j - 1, M, rows, columns, len_walk) + 1

    if j < columns - 1 and M[i][j] < M[i][j + 1]:
        right = longpath(i, j + 1, M, rows, columns, len_walk) + 1

    if i > 0 and j > 0 and M[i][j] < M[i - 1][j - 1]:
        l_up = longpath(i - 1, j - 1, M, rows, columns, len_walk) + 1

    if i > 0 and j < columns - 1 and M[i][j] < M[i - 1][j + 1]:
        r_up = longpath(i - 1, j + 1, M, rows, columns, len_walk) + 1

    if i < rows - 1 and j > 0 and M[i][j] < M[i + 1][j - 1]:
        l_down = longpath(i + 1, j - 1, M, rows, columns, len_walk) + 1

    if i < rows - 1 and j < columns - 1 and M[i][j] < M[i + 1][j + 1]:
        r_down = longpath(i + 1, j + 1, M, rows, columns, len_walk) + 1

    len_walk[i][j] = max(up, max(down, max(left, max(right, max(l_up, max(r_up, max(l_down, max(r_down, 1))))))))
    return len_walk[i][j]                                                  # checks all directions, return max len walk


def longest_walk(M):
    """
    Finds the longest increasing walk in a matrix M
    :time_complexity: O(nm) - optimal
    :auxiliary_space: O(nm) - optimal
        where n is rows and m is columns in matrix M
    :param M: An n×m matrix in form M[i][j] where i is the row and j is the column
    :return:a tuple containing the longest walk length and its path (in terms of (i, j))
    """
    rows = len(M)                                                          # initialise row/col/walk length var
    columns = len(M[0])
    longest = 0

    len_walk = [[-1 for j in range(columns)]for i in range(rows)]          # initialise longest walk var for D.P

    for i in range(rows):                                                  # for each cell in len_walk find the-
        for j in range(columns):                                           # -longest path
            if len_walk[i][j] == -1:                                       # checks if path is already found
                longpath(i, j, M, rows, columns, len_walk)

            longest = max(longest, len_walk[i][j])                         # updates walk length to highest value

    maxi = [0, []]                                                         # initialise var for backtracking

    for row in range(rows):                                                # search len_walk to find last position-
        for column in range(columns):                                      # -for the longest walk and length
            if len_walk[row][column] > maxi[0]:
                maxi[0], maxi[1] = len_walk[row][column], (row, column)    # maxi = (walk len, position)

    visited = [maxi[1]]                                                    # initialise var to track walk

    while maxi[0] > 1:                                                     # loops if maxi is not at start of walk
        c_row = maxi[1][0]                                                 # checks in each direction from maxi-
        c_col = maxi[1][1]                                                 # -to the possible previous position
        if c_col < columns - 1 and len_walk[c_row][c_col] == len_walk[c_row][c_col + 1] + 1:
            visited.append((c_row, c_col + 1))
            maxi[0] += -1
            maxi[1] = (c_row, c_col + 1)

        elif c_col < columns - 1 and c_row < rows - 1 and len_walk[c_row][c_col] == len_walk[c_row + 1][c_col + 1] + 1:
            visited.append((c_row + 1, c_col + 1))
            maxi[0] += -1
            maxi[1] = (c_row + 1, c_col + 1)

        elif c_row < rows - 1 and len_walk[c_row][c_col] == len_walk[c_row + 1][c_col] + 1:
            visited.append((c_row + 1, c_col))
            maxi[0] += -1
            maxi[1] = (c_row + 1, c_col)

        elif c_row < rows - 1 and c_col > 0 and len_walk[c_row][c_col] == len_walk[c_row + 1][c_col - 1] + 1:
            visited.append((c_row + 1, c_col - 1))
            maxi[0] += -1
            maxi[1] = (c_row + 1, c_col - 1)

        elif c_col > 0 and len_walk[c_row][c_col] == len_walk[c_row][c_col - 1] + 1:
            visited.append((c_row, c_col - 1))
            maxi[0] += -1
            maxi[1] = (c_row, c_col - 1)

        elif c_col > 0 and c_row > 0 and len_walk[c_row][c_col] == len_walk[c_row - 1][c_col - 1] + 1:
            visited.append((c_row - 1, c_col - 1))
            maxi[0] += -1
            maxi[1] = (c_row - 1, c_col - 1)

        elif c_row > 0 and len_walk[c_row][c_col] == len_walk[c_row - 1][c_col] + 1:
            visited.append((c_row - 1, c_col))
            maxi[0] += -1
            maxi[1] = (c_row - 1, c_col)

        elif c_row > 0 and c_col < columns - 1 and len_walk[c_row][c_col] == len_walk[c_row - 1][c_col + 1] + 1:
            visited.append((c_row - 1, c_col + 1))
            maxi[0] += -1
            maxi[1] = (c_row - 1, c_col + 1)

    return longest, visited                                                   # return (len walk, path)




