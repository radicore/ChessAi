import chess
from chess import WHITE, BLACK, SQUARES, square_mirror, square_distance
from piece_mapping import *
from constants import *
from bitboard_helper import xray_rook_blockers

# K16_2 uses only 2 evaluations: piece mapping and piece values, K16_1 uses 4 = slower


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


def material_score(BOARD):  # used in depth_handler.py
    score = 0
    for square in SQUARES:
        piece = BOARD.piece_at(square)
        if piece:
            value = PIECE_VALUES[piece.piece_type]
            score += value if piece.color == WHITE else -value

    return score


def is_end_game(BOARD):  # Basic endgame check, if n total pieces are <= 12 then it is an endgame.
    if sum(1 for square in SQUARES if BOARD.piece_at(square)) <= 12:
        return True

    return False


def is_game_over(BOARD):
    if BOARD.is_game_over() or BOARD.is_checkmate() or BOARD.is_stalemate() or BOARD.is_fifty_moves() or BOARD.is_insufficient_material() or BOARD.is_repetition():
        return True
    return False


def n_moves(BOARD, end_game=False):  # Calculates number of legal moves the current side has.
    moves = int(len(list(BOARD.legal_moves)))
    if end_game:
        BOARD.turn = not BOARD.turn
        moves = int(len(list(BOARD.legal_moves)))
        BOARD.turn = not BOARD.turn
    return round(moves / 4) if end_game else round(moves / 10)


def ray_cast(BOARD, starting_square):
    open_squares = 0

    piece = BOARD.piece_at(starting_square).piece_type

    def cast_ray(direction, _open_squares=0):
        # Returns 0 if the first square is an edge, else continue in direction until an edge is found
        if SQUARES[starting_square + direction] in EDGES: return 0
        for i in range(1, 8):
            try:
                new_square = starting_square + direction * i
                if BOARD.piece_at(new_square) is None:
                    _open_squares += 1
                    if SQUARES[new_square] in EDGES:
                        break
                    # print(chess.square_name(new_square))
                else:
                    break
            except IndexError:
                pass

        return _open_squares

    # checks empty squares ahead / behind (in files)
    if piece == ROOK:
        open_squares += cast_ray(NORTH) + cast_ray(SOUTH)

    else:  # bishop
        open_squares += cast_ray(NORTH_EAST) + cast_ray(SOUTH_WEST) + cast_ray(NORTH_WEST) + cast_ray(SOUTH_EAST)

    if open_squares >= 5:  # 5+ empty squares are considered an open file
        return OPEN_FILE
    elif open_squares >= 3:  # 3-4 empty squares are considered semi open file
        return SEMI_FILE
    return -5


"""def paired_pieces(BOARD, ):
    pass  # print(BOARD.rooks)"""


"""def piece_value_increment(material_count):
    pass"""


def distance_translate(squares):
    return distance_dict[squares]


def evaluate(BOARD, end_game=False, engineType=1):
    # Basic checks for game status
    if BOARD.is_stalemate() or BOARD.is_insufficient_material() or BOARD.is_repetition():
        return 0
    elif is_game_over(BOARD):
        return -INF if BOARD.turn == WHITE else INF

    score = 0

    # RP = []  # ray pieces

    for square in SQUARES:
        piece = BOARD.piece_at(square)
        if piece is None: continue  # Is the square occupied?

        if end_game:  # If true, less evaluation is needed

            # For endgames the square mapping is decreased and legal moves increases (for checkmate finding)
            # if piece.piece_type in [ROOK, BISHOP]:
            # RP.append(square)

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)
            score += val if piece.color == WHITE else -val

        elif engineType == 1:  # Slower but more accurate (?) engine

            white_attackers = len(BOARD.attackers(WHITE, square))
            black_attackers = len(BOARD.attackers(BLACK, square))

            val = 0
            """if piece.piece_type == ROOK:
                val -= xray_rook_blockers(BOARD, square)"""

            val += PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game) + abs(white_attackers - black_attackers)
            score += val if piece.color == WHITE else -val

            # score += attack_value
        else:  # Faster but less accurate (?) engine

            val = PIECE_VALUES[piece.piece_type] + square_mapping(piece, square, end_game)
            score += val if piece.color == WHITE else -val

    if engineType == 1 or end_game:
        # ray_val = 0
        # for k in RP: ray_val += ray_cast(BOARD, k)
        val = 0
        if end_game:
            dist = square_distance(BOARD.king(WHITE), BOARD.king(BLACK))
            val = distance_translate(dist)*2  # +n_moves(BOARD, end_game)
            score += val if chess.WHITE == WHITE else -val

        val += n_moves(BOARD, end_game)
        score += val if chess.WHITE == WHITE else -val

    return score
