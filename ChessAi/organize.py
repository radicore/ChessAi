from chess import QUEEN, KNIGHT, ROOK, BISHOP, Board


def order_moves(BOARD: Board, end_game=False):
    high_score_moves = []

    for move in BOARD.legal_moves:
        toSquare = BOARD.piece_at(move.to_square)
        try:
            toSquare = toSquare.piece_type
            fromSquare = BOARD.piece_at(move.from_square).piece_type
            if BOARD.is_capture(move) and toSquare is not None:
                if toSquare >= fromSquare:
                    if toSquare > fromSquare:  # capturing higher valued piece (Great capture, e.g. Knight x Queen)
                        high_score_moves.insert(2, move)
                    elif toSquare == fromSquare:  # capturing same valued piece (Great capture, e.g. Bishop x Bishop)
                        high_score_moves.insert(3, move)
        except AttributeError:
            pass

        if BOARD.is_checkmate():
            return [move]
        elif BOARD.is_into_check(move):
            high_score_moves.insert(0, move)
        elif BOARD.is_castling(move):
            high_score_moves.insert(1, move)
        elif BOARD.is_zeroing(move) and end_game:
            high_score_moves.insert(3, move)
        elif move.promotion == QUEEN:
            high_score_moves.insert(0, move)
        elif move.promotion == KNIGHT:
            high_score_moves.insert(1, move)
        elif move.promotion == BISHOP:
            high_score_moves.insert(2, move)
        elif move.promotion == ROOK:
            high_score_moves.insert(3, move)
        else:
            high_score_moves.append(move)

    return high_score_moves
