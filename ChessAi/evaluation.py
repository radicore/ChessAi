import chess
import numpy as np

# Use numpy for arrays and other values --> (supposedly) quicker processing

# Piece value constants

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# Piece structure tables

pawns_table = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
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
    1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 0, 0, 0, 0, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 0, 0, 0, 0, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1,
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

king_middle_table = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20
]

king_end_table = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -40, -20, -10, -10, -10, -10, -20, -40,
    -30, -10,  10,  20,  20,  7, -10, -30,
    -20, -10,  20,  40,  40,  20, -10, -20,
    -20, -10,  20,  40,  40,  20, -10, -20,
    -30, -10,  10,  20,  20,  10, -10, -30,
    -40, -20, -10, -10, -10, -10, -20, -40,
    -50, -40, -30, -20, -20, -30, -40, -50,
]

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
"""

pawns_table = np.array(pawns_table)
knights_table = np.array(knights_table)
bishops_table = np.array(bishops_table)
rooks_table = np.array(rooks_table)
queens_table = np.array(queens_table)
king_middle_table = np.array(king_middle_table)
king_end_table = np.array(king_end_table)

reversed_pawns = np.array(list(reversed(pawns_table)))
reversed_bishops = np.array(list(reversed(bishops_table)))
reversed_rooks = np.array(list(reversed(rooks_table)))
reversed_end_rooks = np.array(list(reversed(rooks_end_table)))
reversed_king_middle = np.array(list(reversed(king_middle_table)))
reversed_king_end = np.array(list(reversed(king_end_table)))


# squares_bb = np.array(squares_bb)  # centre control maybe... I think mapping above already does this


# Evaluation function: material balance, mobility, king safety, piece mapping, paired bishops

# DONE: material balance, mobility (ENDGAME ONLY), piece mapping (and bb attacked squares mapping)
# FINISHING: king safety, paired bishops


def evaluate_piece(piece, square, end_game):
    piece_type = piece.piece_type
    if piece_type == chess.PAWN:
        return pawns_table[square] if piece.color == chess.WHITE else -reversed_pawns[square]
    if piece_type == chess.KNIGHT:
        return knights_table[square]
    if piece_type == chess.BISHOP:
        return bishops_table[square] if piece.color == chess.WHITE else -reversed_bishops[square]
    if piece_type == chess.ROOK:
        if end_game:
            return reversed_end_rooks[square] if piece.color == chess.WHITE else -reversed_end_rooks[square]
        else:
            return rooks_table[square] if piece.color == chess.WHITE else -reversed_rooks[square]
    if piece_type == chess.QUEEN:
        return queens_table[square]
    if piece_type == chess.KING:
        if end_game:
            return king_end_table[square] if piece.color == chess.WHITE else -reversed_king_end[square]
        else:
            return king_middle_table[square] if piece.color == chess.WHITE else -reversed_king_middle[square]


def check_end_game(BOARD):
    queens = 0
    minors = 0
    count = 0
    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)
        if not piece:
            continue

        if piece.piece_type == chess.QUEEN:
            queens += 1
        if piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT:
            minors += 1

        count += 1

    if queens == 0 or (queens == 2 and minors <= 1) or count == 4:
        return True

    return False


def n_moves(BOARD):  # calculates number of legal moves the current side has
    return len(list(BOARD.legal_moves)) if BOARD.turn == chess.WHITE else -len(list(BOARD.legal_moves))


def evaluate(BOARD, end_game=False, engineType=1):  # initializes all evaluation functions above
    if BOARD.is_stalemate() | BOARD.is_insufficient_material() | BOARD.is_repetition():
        return 0
    elif BOARD.is_checkmate():
        return float("inf") if chess.WHITE else -float("inf")

    score = 0

    control_table = np.zeros((8, 8), dtype=int)

    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)

        if end_game:
            if piece is None:
                continue

            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value
            score += n_moves(BOARD) + evaluate_piece(piece, square, end_game)

        elif engineType == 1:
            # Creates a bitboard of attackers on each square
            white_attackers = BOARD.attackers(chess.WHITE, square)
            black_attackers = BOARD.attackers(chess.BLACK, square)

            if white_attackers:
                control_table[chess.square_rank(square)][chess.square_file(square)] += len(white_attackers)
            if black_attackers:
                control_table[chess.square_rank(square)][chess.square_file(square)] -= len(black_attackers)

            if not piece:
                continue

            # adds piece weight and precomputed scores of the square
            value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value
            score += control_table[chess.square_rank(square)][chess.square_file(square)]
        else:  # switch to faster evaluation (engine 2)
            if not piece:
                continue

            value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value

    # apparently calling n_moves(BOARD) is what slows the program down, so I left it out

    return score
