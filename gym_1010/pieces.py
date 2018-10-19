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
    hand = [rand_rot(np.array(PIECES[[_ for _ in PIECES][np.random.randint(0, 9)]], dtype=int)) for _ in range(3)]
    return hand

def get_keys_to_action(self) -> dict:
        """Return the dictionary of keyboard keys to actions."""
        # Map of actions to ASCI value
        p_1 = ord('1')
        p_2 = ord('2')
        p_3 = ord('3')
        up = ord('w')
        left = ord('a')
        down = ord('s')
        right = ord('d')
        swap = ord('q')
        place = ord('e')
        # A mapping of pressed key combinations to discrete actions
        keys_to_action = {
            (): 0,

            (left, ): 1,

            (right, ): 2,

            (down, ): 3,

            (swap, ): 4,

            (place, ): 5,

            tuple(sorted((up, swap, ))): 6,
            tuple(sorted((up, place, ))): 7,

            tuple(sorted((left, swap, ))): 8,
            tuple(sorted((left, place, ))): 9,

            tuple(sorted((down, swap, ))): 10,
            tuple(sorted((down, place, ))): 11,

            tuple(sorted((right, swap, ))): 12,
            tuple(sorted((right, place, ))): 13,

            tuple(sorted((left, swap, ))): 14,
            tuple(sorted((left, place, ))): 15
        }

        return keys_to_action
