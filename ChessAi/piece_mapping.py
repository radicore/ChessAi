import numpy as np

# Numpy arrays are faster for fetching and storing data

pawns_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 30, 30, 0, 0, 0,
    5, 5, 10, 20, 20, 10, 5, 5,
    10, 10, 20, 25, 25, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0,
]

knights_table = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

bishops_table = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 2, 2, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]

rooks_table = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]

rooks_end_table = [
    1, 2, 1, 1, 1, 1, 2, 1,
    2, 1, 0, 0, 0, 0, 1, 2,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    2, 1, 0, 0, 0, 0, 1, 2,
    1, 2, 1, 1, 1, 1, 2, 1,
]

queens_table = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

queens_end_table = [
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 30, -1, -1, -1, -1, 30, 1,
    1, -1, 0, 0, 0, 0, -1, 1,
    1, -1, 0, 0, 0, 0, -1, 1,
    1, -1, 0, 0, 0, 0, -1, 1,
    1, -1, 0, 0, 0, 0, -1, 1,
    1, 30, -1, -1, -1, -1, 30, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
]

king_middle_table = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    10, 6, 10, 0, 0, 10, 6, 10
]

king_end_table = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -40, -20, -10, -10, -10, -10, -20, -40,
    -30, -10, 20, 20, 20, 20, -10, -30,
    -20, -10, 20, 30, 30, 20, -10, -20,
    -20, -10, 20, 30, 30, 20, -10, -20,
    -30, -10, 20, 20, 20, 20, -10, -30,
    -40, -20, -10, -10, -10, -10, -20, -40,
    -50, -40, -30, -20, -20, -30, -40, -50,
]

pawns_table = np.array(pawns_table)
knights_table = np.array(knights_table)
bishops_table = np.array(bishops_table)
rooks_table = np.array(rooks_table)
rooks_end_table = np.array(rooks_end_table)
queens_table = np.array(queens_table)
queens_end_table = np.array(queens_end_table)
king_middle_table = np.array(king_middle_table)
king_end_table = np.array(king_end_table)

# Negative mapping for black

black_pawns = list(reversed(-pawns_table))
black_bishops = list(reversed(-pawns_table))
black_knights = list(reversed(-knights_table))
black_rooks = list(reversed(-rooks_table))
black_end_rooks = list(reversed(-rooks_end_table))
black_queens = list(reversed(-queens_table))
black_end_queens = list(reversed(-queens_end_table))
black_king_middle = list(reversed(-king_middle_table))
black_king_end = list(reversed(-king_end_table))


"""black_pawns = list(reversed(pawns_table))
black_bishops = list(reversed(pawns_table))
black_knights = list(reversed(knights_table))
black_rooks = list(reversed(rooks_table))
black_end_rooks = list(reversed(rooks_end_table))
black_queens = list(reversed(queens_table))
black_end_queens = list(reversed(queens_end_table))
black_king_middle = list(reversed(king_middle_table))
black_king_end = list(reversed(king_end_table))"""

# Apparently this is what was causing it to play worse moves as black
# The Minimax algorithm tries to minimize and maximize the score so reversing the piece mappings was not needed
"""
black_pawns = -np.array(list(reversed(pawns_table)))
black_bishops = -np.array(list(reversed(bishops_table)))
black_knights = -np.array(list(reversed(knights_table)))
black_rooks = -np.array(list(reversed(rooks_table)))
black_end_rooks = -np.array(list(reversed(rooks_end_table)))
black_queens = -np.array(list(reversed(queens_table)))
black_end_queens = -np.array(list(reversed(queens_end_table)))
black_king_middle = -np.array(list(reversed(king_middle_table)))
black_king_end = -np.array(list(reversed(king_end_table)))
"""
