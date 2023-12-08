from chess import PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING, BB_FILE_A, BB_FILE_H, BB_RANK_8, BB_RANK_1
# from random import getrandbits

# Piece values - pawn and minor pieces depend on each other:
# As n pawns decrease, minor pieces increase
# As n minors decrease, pawns increase

PIECE_VALUES = {
    PAWN: 120,
    KNIGHT: 300,
    BISHOP: 320,  # bishops are generally worth more (can control more squares at once)
    ROOK: 500,
    QUEEN: 900,
    KING: 0
}

EDGES = BB_FILE_A | BB_FILE_H | BB_RANK_8 | BB_RANK_1

for k, v in PIECE_VALUES.items(): PIECE_VALUES[k] = v // 2  # 25, 77, 80, 125, 225 (updated values)

"""
- KNIGHT = ~3 PAWNS
- BISHOP = ~3 PAWNS
- ROOK = (KNIGHT or BISHOP) + 2 PAWNS
- QUEEN = (KNIGHT or BISHOP) + ROOK
"""

INF = 1e6  # Checkmate value

# Bonus values

OPEN_RAY = 10
SEMI_OPEN_RAY = 5

# CONNECTED_ROOKS = 10
# PAIRED_BISHOPS = 20

DOUBLED_PAWNS_PENALTY = 6
ISOLATED_PAWNS_PENALTY = 3
PAWN_CHAIN_BONUS = 3

KING_PAWN_TROPISM = 2

# dictionaries

memory = {}

distance_dict = {7: 1, 6: 2, 5: 3, 4: 4, 3: 5, 2: 6, 1: 7}

# ZOBRIST_HASHES = [getrandbits(64) for _ in range(12*64)]
