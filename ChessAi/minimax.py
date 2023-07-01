from organize import order_moves
from evaluation import *


def minimax_AB(board: chess.Board, depth: int, alpha: int, beta: int, maximizing_player: bool, end_game=False, engineType=2, memo=None):
    if memo is None:
        memo = {}

    key = (hash(board.fen()), depth)

    if key in memo:
        return memo[key]

    if depth == 0 or board.is_game_over() or board.is_checkmate():
        return evaluate(board, end_game, engineType)

    eval_func = max if maximizing_player else min
    best_eval = -INF if maximizing_player else INF

    moves = order_moves(board)

    for move in moves:
        board.push(move)
        evaluation = minimax_AB(board, depth - 1, alpha, beta, not maximizing_player, end_game, engineType, memo)
        board.pop()

        best_eval = eval_func(best_eval, evaluation)

        alpha = max(alpha, evaluation) if maximizing_player else alpha
        beta = min(beta, evaluation) if not maximizing_player else beta

        # print(alpha, beta)
        if beta <= alpha:
            break

    if key not in memo:
        memo[key] = best_eval

    return best_eval
