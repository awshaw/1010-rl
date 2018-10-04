import numpy as np

BOARD_WIDTH = 10
BOARD_HEIGHT = 10
BOX_SIZE = 100
XMARGIN = 10
TOPMARGIN = 10

PIECES = {
    's1': [1],
    's2': np.ones((2,2)),
    's3': np.ones((3,3,)),

}

def new_pieces() -> dict:
    """
    Return new set of pieces (to be used
    after all three previous pieces placed)
    """

    return 