from chess import A1, A2, A3, A4, A5, A6, A7, A8, B1, C1, D1, E1, F1, G1, H1, H2, H3, H4, H5, H6, H7, H8, G8, F8, E8, D8, C8, B8, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING
from random import getrandbits

# Piece values - pawn and minor pieces depend on each other:
# As n pawns decrease, minor pieces increase
# As n minors decrease, pawns increase

PIECE_VALUES = {
    PAWN: 100,
    KNIGHT: 310,
    BISHOP: 320,  # bishops are generally worth more (can control more squares at once)
    ROOK: 500,
    QUEEN: 900,
    KING: 0
}

for k, v in PIECE_VALUES.items():
    PIECE_VALUES[k] = v // 3  # 25, 77, 80, 125, 225 (updated values)

"""
- KNIGHT = ~3 PAWNS
- BISHOP = ~3 PAWNS
- ROOK = (KNIGHT or BISHOP) + 2 PAWNS
- QUEEN = (KNIGHT or BISHOP) + ROOK
"""

INF = 1e6  # Checkmate value

# Directional values

NORTH = 8
SOUTH = -8
EAST = 1
WEST = -1

NORTH_EAST = NORTH + EAST
NORTH_WEST = NORTH + WEST
SOUTH_EAST = SOUTH + EAST
SOUTH_WEST = SOUTH + WEST

EDGES = [
    A1, A2, A3, A4, A5, A6, A7,
    A8, B1, C1, D1, E1, F1, G1,
    H1, H2, H3, H4, H5, H6, H7,
    H8, G8, F8, E8, D8, C8, B8
]

# Bonus values

OPEN_FILE = 20
SEMI_FILE = 10

PAIRED_ROOKS = 10
PAIRED_BISHOPS = 20

# dictionaries

distance_dict = {
    7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7
}

# ZOBRIST_HASHES = [getrandbits(64) for _ in range(12*64)]
