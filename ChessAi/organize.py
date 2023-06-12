import chess


def order_moves(BOARD):
    high_score_moves = []
    for move in BOARD.legal_moves:
        if BOARD.is_capture(move) or BOARD.is_en_passant(move) or (move.promotion == chess.QUEEN or move.promotion == chess.KNIGHT) or BOARD.is_checkmate() or BOARD.is_check():
            if BOARD.is_checkmate():
                return [move]
            if BOARD.is_check():
                high_score_moves.insert(0, move)
            if move.promotion == chess.QUEEN:
                high_score_moves.insert(1, move)
            if BOARD.is_capture(move) or BOARD.is_en_passant(move):
                high_score_moves.insert(2, move)
            if move.promotion == chess.KNIGHT:
                high_score_moves.insert(3, move)
            # ELSE other promotions are useless, so no need to add them (only need QUEEN or KNIGHT)
        else:
            high_score_moves.append(move)  # scores that are not as high are added last

    return high_score_moves
