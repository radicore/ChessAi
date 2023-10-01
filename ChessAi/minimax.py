from organize import order_moves
from evaluation import *
from constants import memory

# condensed alpha beta minimax algorithm


def minimax_AB(board, depth: int, alpha: int, beta: int, maximizing_player: bool, end_game=False, engineType=2):
    if depth == 0 or is_game_over(board):
        return evaluate(board, end_game, engineType)

    key = (hash(board.fen()), depth)  # hashing fen

    if key in memory:
        return memory[key]

    eval_func = max if maximizing_player else min
    best_eval = -INF if maximizing_player else INF

    moves = order_moves(board)

    for move in moves:
        board.push(move)
        evaluation = minimax_AB(board, depth - 1, alpha, beta, not maximizing_player, end_game, engineType)
        board.pop()

        best_eval = eval_func(best_eval, evaluation)

        if maximizing_player:
            if best_eval > alpha:
                alpha = evaluation
        else:
            if best_eval < beta:
                beta = evaluation

        if alpha >= beta:
            return best_eval

    if key not in memory:
        memory[key] = best_eval

    return best_eval
