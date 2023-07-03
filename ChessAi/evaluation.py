import chess
from piece_mapping import *

INF = 1e6

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 310,
    chess.BISHOP: 320,  # bishops are generally worth more (can control more squares at once)
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

"""
- KNIGHT ~3 PAWNS
- BISHOP ~3 PAWNS
- ROOK = KNIGHT or BISHOP + 2 PAWNS
- QUEEN = ROOK + KNIGHT or BISHOP
"""

# Evaluation function: performs calculations based on mobility, n attackers, piece values, positional values
# K16_2 Uses only 2: piece values and positional values compared to K16_1 which uses all 4 (thus more accurate takes longer to calculate)


def square_mapping(piece, square, end_game):
    piece_type = piece.piece_type
    _mapping = []  # used to store square mapping (piece mapping tables)
    if piece_type == chess.PAWN:
        _mapping = PAWNS_END_TABLE if end_game else PAWNS_TABLE
    elif piece_type == chess.KNIGHT:
        _mapping = KNIGHTS_END_TABLE if end_game else KNIGHTS_TABLE
    elif piece_type == chess.BISHOP:
        _mapping = BISHOPS_END_TABLE if end_game else BISHOPS_TABLE
    elif piece_type == chess.ROOK:
        _mapping = ROOKS_END_TABLE if end_game else ROOKS_TABLE
    elif piece_type == chess.QUEEN:
        _mapping = QUEENS_END_TABLE if end_game else QUEENS_TABLE
    elif piece_type == chess.KING:
        _mapping = KINGS_END_TABLE if end_game else KINGS_MIDDLE_TABLE

    # Use chess.square_mirror() since mapping[E4] would return the value on the D4 square
    # Reason behind this? No clue, chess module being funny.

    mapping = []
    for k in range(0, 64):
        mapping.append(_mapping[k] + BASE_SAFETY[k])

    return mapping[chess.square_mirror(square)] if piece.color == chess.WHITE else mapping[square]


def is_end_game(BOARD):  # Basic endgame check, if n total pieces are <= 7 then it is an endgame.
    if sum(1 for square in chess.SQUARES if BOARD.piece_at(square)) <= 7:
        return True

    return False


def n_moves(BOARD, end_game=False):  # Calculates number of legal moves the current side has.
    moves = int(len(list(BOARD.legal_moves)))
    if end_game:
        BOARD.turn = not BOARD.turn
        moves = int(len(list(BOARD.legal_moves)))
        BOARD.turn = not BOARD.turn
    return round(moves) if end_game else round(moves / 4)


def material_score(BOARD):  # used in depth_handler.py
    score = 0
    for square in chess.SQUARES:
        piece = BOARD.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == chess.WHITE else -value

    return score


def evaluate(BOARD, end_game=False, engineType=1):
    # Basic checks for game status
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

            # For endgames the square mapping is decreased and legal moves increases (for checkmate finding)
            value = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)
            score += value if piece.color == chess.WHITE else -value

        elif engineType == 1:  # Slower but more accurate (?) engine
            if piece is None:
                continue

            white_attackers = len(BOARD.attackers(chess.WHITE, square))
            black_attackers = len(BOARD.attackers(chess.BLACK, square))

            if white_attackers < black_attackers:
                attack_value = white_attackers - black_attackers
            else:
                attack_value = black_attackers - white_attackers

            # Adds the piece weight, mapping values and n attackers based on the piece position
            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game) + attack_value
            score += val if piece.color == chess.WHITE else -val

            # score += attack_value
        else:  # Faster but less accurate (?) engine
            if piece is None:
                continue

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)
            score += val if piece.color == chess.WHITE else -val
            # print(chess.square_name(square), chess.piece_name(piece.piece_type), piece.color, val)
            # above value should be zero if symmetrical

    if engineType == 1:
        score += n_moves(BOARD, end_game) if BOARD.turn == chess.WHITE else -n_moves(BOARD, end_game)

    return score
