import chess
from piece_mapping import *

INF = 1e5

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 310,
    chess.BISHOP: 330,  # bishops are generally worth more (endgames and can control more squares at once)
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


def evaluate_piece(piece, square, end_game):
    piece_type = piece.piece_type
    mapping = []  # used to store square mapping (piece mapping tables)
    if piece_type == chess.PAWN:
        mapping = PAWNS_END_TABLE if end_game else PAWNS_TABLE
    elif piece_type == chess.KNIGHT:
        mapping = KNIGHTS_TABLE
    elif piece_type == chess.BISHOP:
        mapping = BISHOPS_TABLE
    elif piece_type == chess.ROOK:
        mapping = ROOKS_END_TABLE if end_game else ROOKS_TABLE
    elif piece_type == chess.QUEEN:
        mapping = QUEENS_END_TABLE if end_game else QUEENS_TABLE
    elif piece_type == chess.KING:
        mapping = KINGS_END_TABLE if end_game else KINGS_MIDDLE_TABLE

    # Use chess.square_mirror() since mapping[E4] would return the value on the D4 square
    # Reason behind this? No clue, chess module being funny.

    return mapping[::-1][square] if piece.color == chess.WHITE else mapping[square]


def check_end_game(BOARD):  # Basic endgame check, if n total pieces are <= 8 then it is an endgame.
    if sum(1 for square in chess.SQUARES if BOARD.piece_at(square)) <= 8:
        return True

    return False


def n_moves(BOARD, current=True):  # Calculates number of legal moves the current side has.
    moves = int(len(list(BOARD.legal_moves)))
    if not current:
        BOARD.turn = not BOARD.turn
        moves = int(len(list(BOARD.legal_moves)))
        BOARD.turn = not BOARD.turn
    return int(moves / 5)


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
            if piece is None:
                continue

            white_attackers = len(BOARD.attackers(chess.WHITE, square))
            black_attackers = len(BOARD.attackers(chess.BLACK, square))

            attack_value = (white_attackers - black_attackers)

            # Adds the piece weight, mapping values and n attackers based on the piece position
            val = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += n_moves(BOARD) if BOARD.turn == chess.WHITE else -n_moves(BOARD)
            score += val if piece.color == chess.WHITE else -val
            score += attack_value
        else:  # Faster but less accurate (?) engine
            if piece is None:
                continue

            val = PIECE_VALUES[piece.piece_type] + evaluate_piece(piece, square, end_game)
            score += val if piece.color == chess.WHITE else -val

    return score
