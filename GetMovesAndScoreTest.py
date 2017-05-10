from GetMovesAndScores import GetMovesAndScores as GMAS
import tensorflow as tf
import chess


b = chess.Board()
move = chess.Move.from_uci('g7g6')
print(move)
b.push(move)
pn = GMAS()
pn.makeMoves(b) #체스 보드를 넣는다.
scores, moves = pn.makeMoves()

print(moves)
print(scores)