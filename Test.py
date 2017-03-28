a = [ 0 * 1 for i in range(100)]

import chess

board1 = chess.Board()
board1.push_san("e3")
moves = board1.legal_moves

print(moves)

print(type(moves))

