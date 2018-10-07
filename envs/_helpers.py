import numpy as np


# Find row/col = 10, update score (+10)
def ten(board):
    for i in range(0,10):
        board


# b = np.array([np.random.randint(0,2,10) for i in range(10)])
def find_squares(board, dim):
    rows = []
    cols = []
    for i in range(10):
        for j in range(2, 11):
            if i + 2 <= 10:
                b = board[i:i + dim, j - dim:j]
                if np.sum(b) == 0:
                    print(b)
                    rows.append([i])
                    cols.append([j - dim])
                    print("Rows: ", i, ":", i+dim-1, 'Cols: ', j-dim+1, ':', j)


def find_vecs(board, dim, rot):
    rows = []
    cols = []

    if rot == 0:
        for i in range(10):
            if i + dim <= 10:
                for j in range(1, 11):
                    k = board[i:i + dim, j - 1:j]
                    if np.sum(k) == 0:
                        print(k)
                        print(i, i + dim, j - 1, j)
                        rows.append([i, i+dim])
                        cols.append([j])

    elif rot == 1:
        for i in range(10):
            for j in range(10):
                if j+dim <= 10:
                    k = board[i, j:j+dim]
                    if np.sum(k) == 0:
                        print(k)
                        print(i, j, j+dim)
                        rows.append([i])
                        cols.append([j])

    else:
        print('Null')

