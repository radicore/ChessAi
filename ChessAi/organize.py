from chess import QUEEN, KNIGHT, ROOK, BISHOP, Board


def order_moves(BOARD: Board):
    high_score_moves = []

    for move in BOARD.legal_moves:
        if BOARD.is_checkmate():
            return [move]
        elif BOARD.is_check():
            high_score_moves.insert(0, move)
        elif BOARD.is_castling(move):
            high_score_moves.insert(2, move)
        elif move.promotion == QUEEN:
            high_score_moves.insert(3, move)
        elif move.promotion == KNIGHT:
            high_score_moves.insert(4, move)
        elif move.promotion == BISHOP:
            high_score_moves.insert(5, move)
        elif move.promotion == ROOK:
            high_score_moves.insert(6, move)
        elif BOARD.is_capture(move) and BOARD.piece_at(move.to_square) is not None:
            if BOARD.piece_at(move.to_square).piece_type >= BOARD.piece_at(move.from_square).piece_type:
                to_capture_val = BOARD.piece_at(move.to_square).piece_type
                piece_capturing_val = BOARD.piece_at(move.from_square).piece_type
                if to_capture_val > piece_capturing_val:  # capturing higher valued piece (Great capture, e.g. Knight x Queen)
                    high_score_moves.insert(7, move)
                else:  # capturing same valued piece (Great capture, e.g. Bishop x Bishop)
                    high_score_moves.insert(8, move)
        else:
            high_score_moves.append(move)

    return high_score_moves
