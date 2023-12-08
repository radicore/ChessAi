from chess import SQUARES, square_mirror, square_distance
from bitboard_helper import *
from piece_mapping import *
from constants import *

# K16_2 uses only 2 evaluations: piece mapping and piece values
# K16_1 uses many = slower


def square_mapping(piece, square, end_game):
    piece_type = piece.piece_type
    mapping = []  # used to store square mapping (piece mapping tables)
    if piece_type == PAWN:
        mapping = PAWNS_END_TABLE if end_game else PAWNS_TABLE
    elif piece_type == KNIGHT:
        mapping = KNIGHTS_END_TABLE if end_game else KNIGHTS_TABLE
    elif piece_type == BISHOP:
        mapping = BISHOPS_END_TABLE if end_game else BISHOPS_TABLE
    elif piece_type == ROOK:
        mapping = ROOKS_END_TABLE if end_game else ROOKS_TABLE
    elif piece_type == QUEEN:
        mapping = QUEENS_END_TABLE if end_game else QUEENS_TABLE
    elif piece_type == KING:
        mapping = KINGS_END_TABLE if end_game else KINGS_MIDDLE_TABLE

    # Use chess.square_mirror() since mapping[E4] would return the value on the D4 square
    # Reason behind this? No clue, chess module being funny.

    return mapping[square_mirror(square)] if piece.color == WHITE else mapping[square]


def is_end_game(BOARD: Board):  # Basic endgame check, if n total pieces are <= 8 then it is an endgame.
    if count(BOARD.occupied) <= 8:
        return True
    return False


def is_game_over(BOARD):
    if BOARD.is_game_over() or BOARD.is_checkmate() or BOARD.is_stalemate() or BOARD.is_fifty_moves() or BOARD.is_insufficient_material() or BOARD.is_repetition():
        return True
    return False


def mobility(BOARD, end_game=False):  # Calculates number of legal moves the current side has.
    if end_game:
        BOARD.turn = not BOARD.turn
        moves = len(list(BOARD.legal_moves))
        BOARD.turn = not BOARD.turn
    else:
        moves = len(list(BOARD.legal_moves))
    return moves / 4 if end_game else moves / 10


def evaluate(BOARD: Board, end_game=False, engineType=1):
    # Basic checks for game status
    if BOARD.is_stalemate() or BOARD.is_insufficient_material() or BOARD.is_repetition():
        return 0
    elif is_game_over(BOARD):
        return -INF if BOARD.turn == WHITE else INF

    score = 0

    for square in SQUARES:
        piece = BOARD.piece_at(square)
        if piece is None: continue  # Is the square occupied?

        if end_game and engineType:  # If true, less evaluation is needed

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)  # K16_2 evaluation for quicker results
            score += val if piece.color == WHITE else -val

        if engineType == 1:  # Slower but more accurate (?) engine

            white_attackers = len(BOARD.attackers(WHITE, square))
            black_attackers = len(BOARD.attackers(BLACK, square))

            attackers = abs(white_attackers - black_attackers)*6

            rookBonus, bishopBonus = 0, 0

            if piece.piece_type == ROOK:
                rookBonus = openFileBonus(BOARD, square)
            elif piece.piece_type == BISHOP:
                bishopBonus = openFileBonus(BOARD, square)

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game) + attackers + rookBonus + bishopBonus

            score += val if piece.color == WHITE else -val
        else:  # Faster but less accurate (?) engine

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)
            score += val if piece.color == WHITE else -val

    if engineType == 1 or end_game:
        val = 0
        if end_game:
            dist = square_distance(BOARD.king(WHITE), BOARD.king(BLACK))
            val += distance_dict[dist]*2

        val += mobility(BOARD, end_game)
        score += val if BOARD.turn == WHITE else -val

        score += isolatedPawns(BOARD) + doubledPawns(BOARD) + kingSafety(BOARD) + pawnChains(BOARD)

    return score
