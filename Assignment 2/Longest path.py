"""Task 2 - Increasing walk"""


def longpath(i, j, M, rows, columns, len_walk):
    if i < 0 or i >= rows or j < 0 or j >= columns:
        return 0

    if len_walk[i][j] != -1:
        return len_walk[i][j]

    up, down, left, right, l_up, r_up, l_down, r_down = -1, -1, -1, -1, -1, -1, -1, -1

    if i > 0 and M[i][j] < M[i - 1][j]:
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
    return len_walk[i][j]


def longest_walk(M):
    rows = len(M)
    columns = len(M[0])
    longest = 0

    len_walk = [[-1 for j in range(columns)]for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if len_walk[i][j] == -1:
                longpath(i, j, M, rows, columns, len_walk)

            longest = max(longest, len_walk[i][j])

    print (len_walk)

    maxi = [0, []]

    for row in range(rows):
        for column in range(columns):
            if len_walk[row][column] > maxi[0]:
                maxi[0], maxi[1] = len_walk[row][column], (row, column)

    visited = [maxi[1]]

    print(maxi)

    while maxi[0] > 1:
        c_row = maxi[1][0]
        c_col = maxi[1][1]
        print(maxi[0])
        print (c_row, c_col)
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

    return longest, visited


print(longest_walk([[1,2,3], [4,5,6], [7,8,9]]))



