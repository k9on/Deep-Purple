import chess
from GetBoardString import get_BoardString as GB
from MakeLegalMoves import make
import Tree

tmp = chess.Board()

tmpStr = GB(tmp)

tree = Tree.tree()

root = tree.play_tree(tmpStr)

#
# import chess
# from GetBoardString import get_BoardString as GB
# from MakeLegalMoves import make
# import Node
#
# tmp=chess.Board()
#
# tmpstr = GB(tmp)
#
# print(tmpstr)
#
# print("AA")
#
# board2 = chess.Board(tmpstr)
#
# board2.push_san("c4")
#
# legal = board2.legal_moves
#
# legal = str(legal)
#
# print(type(legal))
# print(legal)
#
# legal = make(legal)
#
# print(legal)
#
# node = Node.node()
#
# (node.get_Child()).append(1)
#
# print(node.get_Child())