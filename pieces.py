import numpy as np

PIECES = {
	# Squares
    's1': np.ones((1, 1)),

    's2': np.ones((2, 2)),

    's3': np.ones((3, 3)),

    # L's
    'l2': np.array([[1, 0],
    				[1, 1]]),

    'l3': np.array([[1, 0, 0],
    				[1, 0, 0],
    				[1, 1, 1]]),

    # Vertical/horizontal's'
    'ln2': np.array([[1],
    				 [1]]),

    'ln3': np.array([[1],
    				 [1],
    				 [1]]),

    'ln4': np.array([[1],
    				 [1],
    				 [1],
    				 [1]]),

    'ln5': np.array([[1],
    				 [1],
    				 [1],
    				 [1],
    				 [1]])
}


def rand_rot(piece):
    # rotations: [0, 90, 180, 270]
    times = np.random.randint(0, 4)

    return np.rot90(piece, times).astype(int)


def rand_hand():
    # return a hand of 3 random pieces with random rotations
    hand = [np.array(PIECES[[_ for _ in PIECES][np.random.randint(0, 9)]], dtype=int) for _ in range(3)]
    return hand

def hand_massage(hand, p):
    pass
