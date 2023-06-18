from chess import QUEEN, KNIGHT, ROOK, BISHOP


def order_moves(BOARD):
    high_score_moves = []
    for move in BOARD.legal_moves:
        if BOARD.is_capture(move) or BOARD.is_en_passant(move) or (move.promotion in [QUEEN, KNIGHT, ROOK, BISHOP]) or BOARD.is_checkmate() or BOARD.is_check():
            if BOARD.is_checkmate():
                return [move]
            elif BOARD.is_check():
                high_score_moves.insert(0, move)
            elif BOARD.is_capture(move) or BOARD.is_en_passant(move):
                high_score_moves.insert(1, move)
            elif move.promotion == QUEEN:
                high_score_moves.insert(2, move)
            elif move.promotion == KNIGHT:
                high_score_moves.insert(3, move)
            elif move.promotion == BISHOP:
                high_score_moves.insert(4, move)
            elif move.promotion == ROOK:
                high_score_moves.insert(5, move)
        else:
            high_score_moves.append(move)  # scores that are not as high are added last

    return high_score_moves
