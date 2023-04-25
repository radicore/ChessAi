import numpy as np

# Numpy arrays are faster for fetching and storing data

# Bro the tables are inverted, h2h3 is left side

pawns_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 5, 20, 0, 0, 0,
    5, 0, 0, 20, 200, 0, 0, 5,
    5, 3, 5, 5, 5, 5, 5, 3,
    -1, -1, -1, -1, -1, -1, -1, -1,
    0, 0, 0, 0, 0, 0, 0, 0,
]


knights_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, -2, 0, 0, -2, 0, 0,
    0, 0, 0, -2, -2, 0, 0, 0,
    5, 0, 0, 2, 2, 0, 0, 5,
    0, 0, 12, 0, 0, 10, 0, 0,
    0, 0, 0, 5, 5, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]


bishops_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    -2, -8, -2, -2, -2, -2, -8, -2,
    -2, -8, -2, 0, 0, -2, -8, -2,
    0, 0, 3, 1, 1, 3, 0, 0,
    0, 5, 0, 2, 2, 0, 5, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
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
    -10, 0, 0, 0, 0, 0, 0, -10,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 0, 0, 0, 0, -5,
    -10, 0, -1, 0, 0, 0, -1, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, 0, 30, 30, -10, -10, -20
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


pawns_table = list(reversed(np.array(pawns_table)))
knights_table = list(reversed(np.array(knights_table)))
bishops_table = list(reversed(np.array(bishops_table)))
rooks_table = list(reversed(np.array(rooks_table)))
rooks_end_table = list(reversed(np.array(rooks_end_table)))
queens_table = list(reversed(np.array(queens_table)))
queens_end_table = list(reversed(np.array(queens_end_table)))
king_middle_table = list(reversed(np.array(king_middle_table)))
king_end_table = list(reversed(np.array(king_end_table)))

# Negative mapping for black

black_pawns = pawns_table
black_knights = knights_table
black_bishops = bishops_table
black_rooks = rooks_table
black_end_rooks = rooks_end_table
black_queens = queens_table
black_end_queens = queens_end_table
black_king_middle = king_middle_table
black_king_end = king_end_table


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

"""
pawns_table = [1, 1, 3, 2, 1, 3, 1, 0, 8, 34, 20, 10, 11, 31, 32, 4, 116, 464, 928, 166, 335, 373, 453, 73, 238, 1016, 1313, 2884, 1183, 813, 864, 211, 219, 1221, 1288, 3187, 1561, 920, 890, 300, 132, 447, 863, 363, 522, 613, 611, 112, 7, 25, 15, 19, 24, 56, 52, 2, 0, 0, 6, 5, 3, 5, 1, 0]

knights_table = [12, 3, 25, 6, 2, 10, 3, 2, 41, 69, 22, 25, 7, 82, 14, 12, 10, 96, 346, 78, 136, 71, 108, 32, 32, 37, -54, -887, 112, 94, 67, -2, -32, -88, 80, 463, 38, -74, -61, -4, -6, -50, -338, -76, -167, -62, -104, -37, -17, -63, -34, -9, -63, -96, -32, -21, -10, 3, -27, 2, 3, -23, 0, -6]

bishops_table = [11, 13, 4, -8, -7, 69, 8, -2, 86, 150, 29, 83, 86, 66, 199, 42, 63, 85, 398, 133, 176, 284, 78, 48, 32, -12, -293, -24, -73, -80, 25, 32, -18, -11, 117, 45, 67, 56, -6, -34, -93, -81, -321, -83, -169, -297, -117, -48, -59, -160, -46, -90, -164, -112, -206, -57, 0, -18, 25, 4, 4, -57, 0, -3]

rooks_table = [24, -4, 54, 33, 97, 27, 10, 8, 121, 173, 74, 5, 37, 94, 80, 78, 52, 70, 66, 12, 19, 56, 67, 35, 40, 1, 30, -42, -9, -2, 22, 47, -77, -31, -25, -75, -46, -27, -11, -38, -81, -60, -62, -69, -49, -13, -77, -48, -151, -128, -62, -47, -36, -112, -80, -67, -65, -20, -50, -45, -99, -44, -6, -6]

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

queens_table = [-19, -6, -37, 55, -36, -4, -2, 2, 92, 109, -4, -40, -57, 52, 28, 30, 68, 19, -47, -156, -59, -85, 59, 45, 20, 7, -126, -162, -49, -2, -10, 52, -31, -25, 49, 55, 51, -45, 6, -52, -71, -48, -8, 99, -19, 82, -58, -68, -94, -42, -21, 45, 116, -43, -25, -44, 38, 10, 3, -129, 37, 17, -4, -9]

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

king_middle_table = [-5, -3, -21, -42, -32, -79, -14, -2, -1, -17, -15, -54, -48, -96, -184, -28, -1, -6, -15, -42, -44, -84, -38, -17, 7, -9, -6, -5, -12, -30, -29, 7, -5, -4, 10, 6, 29, 21, 25, 12, 0, 3, 12, 18, 47, 83, 52, 27, -1, 20, 28, 76, 67, 126, 230, 34, -3, 4, 11, 117, 34, 93, 13, 8]

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
"""