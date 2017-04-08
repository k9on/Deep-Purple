import chess
import Board2Array as BA
b = chess.Board()

print(b)

ba = BA.Board2Array()

b = ba.board2array(b)

print(b)


