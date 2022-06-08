from typing import List


def print_matrix(mat: List[List[int]]):
    for row in mat:
        print(''.join(str(row).split(','))[1:-1])


def right(row_index, col_index, value, n_rows, n_cols):
    while col_index < n_cols and M[row_index][col_index] == -1:
        M[row_index][col_index] = value
        value += 1
        col_index += 1

    col_index -= 1

    if M[row_index+1][col_index] == -1:
        down(row_index+1, col_index, value, n_rows, n_cols)


def down(row_index, col_index, value, n_rows, n_cols):
    while row_index < n_rows and M[row_index][col_index] == -1:
        M[row_index][col_index] = value
        value += 1
        row_index += 1

    row_index -= 1

    if M[row_index][col_index-1] == -1:
        left(row_index, col_index-1, value, n_rows, n_cols)


def left(row_index, col_index, value, n_rows, n_cols):
    while n_cols >= 0 and M[row_index][col_index] == -1:
        M[row_index][col_index] = value
        value += 1
        col_index -= 1

    col_index += 1

    if M[row_index-1][col_index] == -1:
        up(row_index-1, col_index, value, n_rows, n_cols)


def up(row_index, col_index, value, n_rows, n_cols):
    while n_rows >= 0 and M[row_index][col_index] == -1:
        M[row_index][col_index] = value
        value += 1
        row_index -= 1

    row_index += 1

    if M[row_index][col_index+1] == -1:
        right(row_index, col_index+1, value, n_rows, n_cols)


if __name__ == '__main__':
    n = int(input())
    m = n
    M = [[-1]*m for _ in range(n)]

    right(row_index=0, col_index=0, value=1, n_rows=n, n_cols=m)

    M_sum = M.copy()
    del M
    for i, row in enumerate(M_sum):
        for j, v in enumerate(row):
            M_sum[i][j] = sum([int(digit) for digit in str(v)])

    print_matrix(M_sum)