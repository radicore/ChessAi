import random
import multiprocessing as mp

from organize import order_moves
from minimax import minimax_AB
from evaluation import *


def material_count(BOARD):  # adds up how many pieces there are all together (to assist set_depth)
    return count(BOARD.occupied)


def set_depth(BOARD: Board):
    mc = material_count(BOARD)

    mobilityWhite = len(list(BOARD.legal_moves))
    BOARD.turn = not BOARD.turn
    mobilityBlack = len(list(BOARD.legal_moves))
    BOARD.turn = not BOARD.turn

    baseMobility = mobilityWhite+mobilityBlack

    if BOARD.fen() in\
            ["8/8/8/8/3K4/2R5/1k6/8 w - - 0 1",
             "8/1k6/2R5/3K4/8/8/8/8 w - - 0 1",
             "8/6k1/5R2/4K3/8/8/8/8 w - - 0 1",
             "8/8/8/8/4K3/5R2/6k1/8 w - - 0 1"]:
        return 10
    else:
        if mc <= 13:
            if baseMobility <= 10 and mc <= 4:
                depth = 6
            elif baseMobility <= 25:
                depth = 5
            elif baseMobility <= 45 or count(BOARD.queens | BOARD.rooks | BOARD.bishops) <= 2:
                depth = 4
            else:
                depth = 3
        else:
            depth = 3

    print(f"\nDEPTH SEARCH = {depth}\n")

    return depth


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    memory.clear()  # clears memory from previous searches (cleanup)

    step = 1

    best_move = None

    # Faster if you put best_eval, alpha and beta here than within the loop

    if max_depth == 10: step = 10  # for known position (rook + king)
    if end_game: PIECE_VALUES[PAWN] = 250

    moves = order_moves(BOARD)

    with mp.Pool(processes=processes) as pool:
        for depth in range(1, max_depth+1, step):
            best_eval = -INF if BOARD.turn else INF
            alpha = -INF
            beta = INF
            results = []

            if best_move in moves:  # best move from previous iteration pushed as first move
                moves.remove(best_move)
                moves.insert(0, best_move)

            for move in moves:
                BOARD.push(move)
                result = pool.apply_async(minimax_AB, (BOARD.copy(), depth, alpha, beta, BOARD.turn, end_game, engineType))
                results.append((move, result))
                BOARD.pop()

            for result in results:
                move, EVAL = result[0], result[1].get()

                alpha = max(alpha, EVAL) if BOARD.turn else alpha
                beta = min(beta, EVAL) if not BOARD.turn else beta

                # print(alpha, beta)
                if BOARD.turn == BLACK:
                    true_depth = (depth+1 // 2)
                else:
                    true_depth = (depth+1 // 2)

                if BOARD.turn:
                    if EVAL > best_eval:
                        if debug:
                            print("Depth", depth, "Evaluation:", round(best_eval / 100, 2), "Best move:", best_move)
                        best_eval = EVAL
                        best_move = move
                        if EVAL == INF:
                            pool.terminate(), pool.join()  # waits for the process to finish before exiting
                            if debug:

                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return best_move, EVAL
                else:
                    if EVAL < best_eval:
                        if debug:
                            print("Depth", depth, "Evaluation:", round(best_eval / 100, 2), "Best move:", best_move)
                        best_eval = EVAL
                        best_move = move
                        if EVAL == -INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return best_move, EVAL

            if best_move is None:  # no point in searching for best moves if there is 1 move available
                return random.choice(list(BOARD.legal_moves)), best_eval

            if debug: print("Depth", depth, "Evaluation:", round(best_eval / 100, 2), "Best move:", best_move)

    return best_move, best_eval


