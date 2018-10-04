import numpy as np

board = np.zeros((10,10))


# Convert piece to 10x10 matrix.
# This takes into account that the agent
# has decided where to place a given piece.
def convert_piece(p):
    tmp = np.zeros((10,10))

# Find row/col = 10, update score (+10)
def TenTen(board):
    for i in range(0,10):
        board