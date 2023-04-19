import chess

from minimax import minimax_AB

DEFAULT = 2

corresponding_MD = {
    3: 6,
    4: 5,
    range(5, 8): 4,
    range(8, 33): 3
}


def material_count(BOARD):
    count = sum(1 for square in chess.SQUARES if BOARD.piece_at(square))
    return count


def order_moves(BOARD):
    ordered_legal_moves = []
    for move in BOARD.legal_moves:
        if BOARD.is_capture(move) or (move.promotion == chess.QUEEN or move.promotion == chess.KNIGHT) or BOARD.is_checkmate() or BOARD.is_check():
            if BOARD.is_checkmate():
                return [move]
            if BOARD.is_check():
                ordered_legal_moves.insert(0, move)
            if move.promotion == chess.QUEEN:
                ordered_legal_moves.insert(1, move)
            if BOARD.is_capture(move):
                ordered_legal_moves.insert(2, move)
            if move.promotion == chess.KNIGHT:
                ordered_legal_moves.insert(3, move)
            else:
                ordered_legal_moves.insert(4, move)
        else:
            ordered_legal_moves.append(move)

    return ordered_legal_moves


def set_depth(BOARD, engineType=1) -> int:  # precaution incase it breaks
    try:
        if engineType == 2:
            corresponding_MD1 = {
                3: 8,
                4: 7,
                range(5, 8): 5,
                range(8, 33): 3
            }
            for key in corresponding_MD1:
                if isinstance(key, int) and key == material_count(BOARD):
                    return corresponding_MD1[key]
                elif isinstance(key, range) and material_count(BOARD) in key:
                    return corresponding_MD1[key]
        else:
            for key in corresponding_MD:
                if isinstance(key, int) and key == material_count(BOARD):
                    return corresponding_MD[key]
                elif isinstance(key, range) and material_count(BOARD) in key:
                    return corresponding_MD[key]
    except KeyError:
        raise f"Material count {material_count(BOARD)} does not exist in table! Set depth to {DEFAULT}"
        # This should never happen, but just incase I mess something up


def optimal_move(max_depth, BOARD, black=False, end_game=False, engineType=1, debug=False):
    # Iterative deepening
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    max_eval = float('-inf')

    for depth in range(1, max_depth + 1):
        moves = order_moves(BOARD)
        for move in moves:
            BOARD.push(move)
            EVAL = minimax_AB(BOARD, depth, alpha, beta, black, end_game=end_game, engineType=engineType)
            BOARD.pop()
            if EVAL > max_eval:
                if EVAL == float("inf") and debug:
                    print("FORCED CHECKMATE FOUND IN", depth, "MOVE(S)")
                max_eval = EVAL
                best_move = move

        if debug:
            print("Depth", depth, "evaluation:", max_eval, "best move:", best_move)
        if max_eval == float("inf"):
            return best_move, max_eval
    return best_move, max_eval


board = chess.Board()
