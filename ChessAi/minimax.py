import random

from organize import order_moves
from evaluation import *
from constants import memory
from chess import Board

# condensed alpha beta minimax algorithm


def minimax_AB(board: Board, depth: int, alpha: int, beta: int, maximizing_player: bool, end_game: bool, engineType: int):
    if depth == 0 or is_game_over(board):
        # return quiescence(board, 2, -beta, -alpha, end_game, engineType)
        return evaluate(board, end_game, engineType)

        # return quiescence(board, 2, -beta, -alpha, end_game, engineType)  # this works but is very slow and IDK if it is correct

    key = (hash(board.fen()), depth)  # hashing fen

    if key in memory:
        return memory[key]

    eval_func = max if maximizing_player else min
    best_eval = -INF if maximizing_player else INF

    for move in order_moves(board, end_game):
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


def quiescence(board: Board, depth: int, alpha: int, beta: int, end_game: bool, engineType: int):
    stand_pat = evaluate(board, end_game, engineType)

    if is_game_over(board) or depth == 0:
        return stand_pat

    if stand_pat >= beta:
        return beta

    if alpha < stand_pat:
        alpha = stand_pat

    moves = [move for move in list(board.legal_moves) if board.is_capture(move) or board.is_into_check(move)]

    if len(moves) == 0:
        return stand_pat

    for move in moves:
        board.push(move)
        score = -quiescence(board, depth - 1, -beta, -alpha, end_game, engineType)
        board.pop()

        if score >= beta:
            return beta

        if score > alpha:
            alpha = score

    return alpha



"""def quiescence(board: Board, alpha: int, beta: int, end_game=False, engineType=2):
    stand_pat = evaluate(board, end_game, engineType)

    if stand_pat >= beta:
        return beta

    moves = [move for move in list(board.legal_moves) if board.is_capture(move) or board.is_castling(move)]

    if len(moves) == 0:
        return stand_pat


    if alpha < stand_pat:
        alpha = stand_pat

    for move in moves:
        board.push(move)
        evaluation = -quiescence(board, -alpha, -beta, end_game, engineType)
        board.pop()
        if evaluation >= beta:
            return beta
        if evaluation > alpha:
            alpha = evaluation

    return alpha
"""