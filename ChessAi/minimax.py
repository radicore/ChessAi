from organize import order_moves
from evaluation import evaluate


def minimax_AB(board, depth, alpha, beta, maximizing_player, end_game=False, engineType=2, memo={}):
    key = (hash(board.fen()), depth)

    if key in memo:
        return memo[key]

    if depth == 0 or board.is_game_over() or board.is_checkmate():
        return evaluate(board, end_game=end_game, engineType=engineType)

    eval_func = max if maximizing_player else min
    eval_value = float('-inf') if maximizing_player else float('inf')

    moves = order_moves(board)

    for move in moves:
        board.push(move)
        evaluation = minimax_AB(board, depth - 1, alpha, beta, not maximizing_player, end_game, engineType, memo)
        board.pop()
        eval_value = eval_func(eval_value, evaluation)
        alpha = max(alpha, evaluation) if maximizing_player else alpha
        beta = min(beta, evaluation) if not maximizing_player else beta
        if beta <= alpha:
            break

    if key not in memo:
        memo[key] = eval_value

    return eval_value
