import chess
import numpy as np
from piece_mapping import *

# Use numpy for quicker storing and retrieving data

# Piece value constants

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}


# Evaluation function: material balance, mobility (ENDGAME ONLY), king safety, piece mapping, paired bishops

# DONE: material balance, mobility, piece mapping (and bitboard attacked squares)
# FINISHING: king safety, paired bishops


def evaluate_piece(piece, square, end_game):  # Evaluates piece type & position on the mapping boards defined above
    piece_type = piece.piece_type
    mapping = []
    if piece_type == chess.PAWN:
        mapping = pawns_table if piece.color == chess.WHITE else reversed_pawns
    if piece_type == chess.KNIGHT:
        mapping = knights_table if piece.color == chess.WHITE else reversed_knights
    if piece_type == chess.BISHOP:
        mapping = bishops_table if piece.color == chess.WHITE else reversed_bishops
    if piece_type == chess.ROOK:
        if end_game:
            mapping = rooks_end_table if piece.color == chess.WHITE else reversed_end_rooks
        else:
            mapping = rooks_table if piece.color == chess.WHITE else reversed_rooks
    if piece_type == chess.QUEEN:
        if end_game:
            mapping = queens_end_table if piece.color == chess.WHITE else reversed_end_queens
        else:
            mapping = queens_table if piece.color == chess.WHITE else reversed_queens
    if piece_type == chess.KING:
        if end_game:
            mapping = king_end_table if piece.color == chess.WHITE else reversed_king_end
        else:
            mapping = king_middle_table if piece.color == chess.WHITE else reversed_king_middle

    return mapping[square]


def check_end_game(BOARD):  # Basic end-game check, if n total pieces are <= 6 then it is an endgame.
    # Why <= 6? Because the legal moves function takes a lot of processing time, else I would set this higher
    if sum(1 for square in chess.SQUARES if BOARD.piece_at(square)) <= 6:
        return True

    return False


def n_moves(BOARD):  # Calculates number of legal moves the current side has. (+) white & (-) black
    return len(list(BOARD.legal_moves)) if BOARD.turn == chess.WHITE else -len(list(BOARD.legal_moves))


def evaluate(BOARD, end_game=False, engineType=1):  # Initializes all evaluation functions above
    # Basic checks for end games
    if BOARD.is_stalemate() | BOARD.is_insufficient_material() | BOARD.is_repetition():
        return 0
    elif BOARD.is_checkmate():
        return float("inf") if BOARD.turn == chess.WHITE else -float("inf")

    score = 0

    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)

        if end_game:  # If true, less evaluation is needed
            if piece is None:  # Is there a piece on the square?
                continue

            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value
            score += n_moves(BOARD) + evaluate_piece(piece, square, end_game) * 5

        elif engineType == 1:  # Slower but more accurate (?) engine
            control_table = np.zeros((8, 8), dtype=int)
            # Creates a bitboard of the number of attackers on each square (including non-occupied squares)
            white_attackers = BOARD.attackers(chess.WHITE, square)
            black_attackers = BOARD.attackers(chess.BLACK, square)

            if white_attackers:
                control_table[chess.square_rank(square)][chess.square_file(square)] += len(white_attackers)
            if black_attackers:
                control_table[chess.square_rank(square)][chess.square_file(square)] -= len(black_attackers)

            if not piece:
                continue

            # Adds the piece weight, mapping values and n attackers based on the piece position
            value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value
            score += control_table[chess.square_rank(square)][chess.square_file(square)]  # adds attackers
        else:  # Faster but less accurate (?) engine
            if not piece:
                continue

            value = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value

    return score
