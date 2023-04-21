import numpy as np

pawns_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
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
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
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
    1, 2, 1, 1, 1, 1, 2, 1,
    2, 1, 0, 0, 0, 0, 1, 2,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    2, 1, 0, 0, 0, 0, 1, 2,
    1, 2, 1, 1, 1, 1, 2, 1,
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
    -30, -10, 10, 20, 20, 10, -10, -30,
    -20, -10, 20, 30, 30, 20, -10, -20,
    -20, -10, 20, 30, 30, 20, -10, -20,
    -30, -10, 10, 20, 20, 10, -10, -30,
    -40, -20, -10, -10, -10, -10, -20, -40,
    -50, -40, -30, -20, -20, -30, -40, -50,
]


# Piece structure tables in piece_mapping.py

# Reversed & inverted tables for black piece mapping
reversed_pawns = -np.array(list(reversed(pawns_table)))
reversed_bishops = -np.array(list(reversed(bishops_table)))
reversed_knights = -np.array(list(reversed(knights_table)))
reversed_rooks = -np.array(list(reversed(rooks_table)))
reversed_end_rooks = -np.array(list(reversed(rooks_end_table)))
reversed_queens = -np.array(list(reversed(queens_table)))
reversed_end_queens = -np.array(list(reversed(queens_end_table)))
reversed_king_middle = -np.array(list(reversed(king_middle_table)))
reversed_king_end = -np.array(list(reversed(king_end_table)))

pawns_table = np.array(pawns_table)
knights_table = np.array(knights_table)
bishops_table = np.array(bishops_table)
rooks_table = np.array(rooks_table)
rooks_end_table = np.array(rooks_end_table)
queens_table = np.array(queens_table)
queens_end_table = np.array(queens_end_table)
king_middle_table = np.array(king_middle_table)
king_end_table = np.array(king_end_table)

# Converting to numpy array makes it slightly faster to fetch data

"""
squares_bb = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 5, 5, 5, 5, 0, 0,
    0, 0, 5, 10, 10, 5, 0, 0,
    0, 0, 5, 10, 10, 5, 0, 0,
    0, 0, 5, 5, 0, 5, 5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]

squares_bb = np.array(squares_bb)  # centre control maybe... I think mapping above already does this
"""
