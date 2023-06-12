import chess

from piece_mapping import *
from directions import *

# Piece value constants

INF = 999999

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,  # bishops are generally worth more (endgames and can control more squares at once)
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

"""
KNIGHT ~3 PAWNS
BISHOP ~3 PAWNS
ROOK ~5 PAWNS = KNIGHT/BISHOP + 2 PAWNS
QUEEN ~8 (ALL) PAWNS = ROOK + KNIGHT/BISHOP
"""

# Evaluation function: material balance, mobility (ENDGAME ONLY), king safety, piece mapping, paired bishops

# DONE: material balance, mobility, piece mapping (and bitboard attacked squares)
# FINISHING: king safety, paired bishops

# Small directional variables


def evaluate_piece(piece, square, end_game):
    piece_type = piece.piece_type
    mapping = []  # global variable for the map assignment below (depending on the piece type)
    if piece_type == chess.PAWN:
        mapping = pawns_end_table if end_game else pawns_table
    elif piece_type == chess.KNIGHT:
        mapping = knights_table
    elif piece_type == chess.BISHOP:
        mapping = bishops_table
    elif piece_type == chess.ROOK:
        mapping = rooks_end_table if end_game else rooks_table  # if endgame, then mapping should be altered
    elif piece_type == chess.QUEEN:
        mapping = queens_end_table if end_game else queens_table
    elif piece_type == chess.KING:
        mapping = king_end_table if end_game else king_middle_table

    return mapping[chess.square_mirror(square)] if piece.color == chess.WHITE else mapping[square]

    # print(f" MAPPING VALUE {value}")  # for symmetrical mapping, this value should be zero (equal)

    # For some reason getting the square for white normally is inverted, so I have to revert using square_mirror()
    # Mapping[chess.square_mirror(square)] accounts for white and mapping[square] accounts for black
    # Depth may affect this result


def check_end_game(BOARD):  # Basic endgame check, if n total pieces are <= 10 then it is an endgame.
    if sum(1 for square in chess.SQUARES if BOARD.piece_at(square)) <= 10:
        return True

    return False


def n_moves(BOARD):  # Calculates number of legal moves the current side has. (+) white & (-) black
    BOARD.turn = not BOARD.turn
    moves = len(list(BOARD.legal_moves))
    BOARD.turn = not BOARD.turn
    return moves


def material_score(BOARD):  # used in depth_handler.py
    score = 0
    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value

    return score


def evaluate(BOARD, end_game=False, engineType=1):  # Initializes all evaluation functions above
    # Basic checks for end games
    if BOARD.is_stalemate() | BOARD.is_insufficient_material() | BOARD.is_repetition():
        return 0
    elif BOARD.is_checkmate():
        return -INF if BOARD.turn == chess.WHITE else INF

    score = 0

    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)
        if end_game:  # If true, less evaluation is needed
            if piece is None:  # Is the square occupied?
                continue
            value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value

        elif engineType == 1:  # Slower but more accurate (?) engine
            control_table = np.zeros((8, 8), dtype=int)
            # Creates a bitboard of the number of attackers on each square (including non-occupied squares)
            white_attackers = len(BOARD.attackers(chess.WHITE, square))
            black_attackers = len(BOARD.attackers(chess.BLACK, square))

            if white_attackers > 1:
                control_table[chess.square_rank(square)][chess.square_file(square)] -= white_attackers
            if black_attackers > 1:
                control_table[chess.square_rank(square)][chess.square_file(square)] += black_attackers

            if piece is None:
                continue

            # Adds the piece weight, mapping values and n attackers based on the piece position
            val = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += val if piece.color == chess.WHITE else -val
            score += control_table[chess.square_rank(square)][chess.square_file(square)]  # adds attackers
        else:  # Faster but less accurate (?) engine
            if piece is None:
                continue

            val = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += val if piece.color == chess.WHITE else -val

    return score
