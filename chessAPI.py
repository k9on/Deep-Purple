# 이 파일은 chess 와 chess.png 패키지의 자주 쓰는 메소드들을 정리한 파일로서
# 실제 소스들과는 전혀 무관하며, 참고용만으로 쓰임
'''
>>> board = chess.Board()

>>> board.legal_moves 
<LegalMoveGenerator at ... (Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, ...)>

>>> chess.Move.from_uci("a8a1") in board.legal_moves
False

>>> board.push_san("e4")
Move.from_uci('e2e4')

>>> board.is_checkmate()
True

>>> board
Board('r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4')

>>> Nf3 = chess.Move.from_uci("g1f3")

>>> board.push(Nf3)  # Make the move

>>> board.pop()  # Unmake the last move
Move.from_uci('g1f3')

>>> board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
>>> print(board)
r . b q k b . r
p p p p . Q p p
. . n . . n . .
. . . . p . . .
. . B . P . . .
. . . . . . . .
P P P P . P P P
R N B . K . N R


#######################################################################################################################
###################################### 게임 오버 상태 체크 ############################################################
>>> board.is_stalemate() # 교착상태인지 아닌지, 교착상태이면 게임이 승자없이 무승부로 끝남
False
>>> board.is_insufficient_material() # 재료가 부족함? 말이 부족해서 교착상태는 아니나, 체크메이트 상황으로 이끌 수 있는 수준
False
>>> board.is_game_over() # 게임이 끝났는지 아닌지 
True


#######################################################################################################################
################################ 무승부 상황을 체크 ###################################################################
>>> board.can_claim_threefold_repetition() # 상중반복이 주장가능한가? 체스 룰상으로 3중반복이 일어나면 무승부를 주장할 수 있다.
False

규칙의 내용은 위와 같이 '정확히 같은 상황이 3번 반복되어 나타났거나 나타나려고 할 때 /
해당 차례의 경기자가 무승부를 선언할 수 있다'는 것입니다. 자동으로 무승부가 되는 건 아니며 상황이 3번 이상
반복된 후 경기자가 자기 차례에 무승부를 선언할 권리가 있다는 것입니다. 반드시 연속적인 수로 나타나야 하는 것은 아닙니다. 


>>> board.halfmove_clock 
0

>>> board.can_claim_fifty_moves()
False
>>> board.can_claim_draw()
False


#######################################################################################################################
2014 년 7 월의 새로운 규칙에 따라 5 배의 반복이 발생하거나 전당포 푸시 또는 캡처없이 75 개의 이동이있는 경우 게임이 종료됩니다
(소유권 주장 없이도). 게임을 종료하는 다른 방법이 우선합니다.


>>> board.is_fivefold_repetition()
False

>>> board.is_seventyfive_moves()
False
########################################################################################################################
#####################################Detects checks and attacks.########################################################

>>> board.is_check()
True

>>> board.is_attacked_by(chess.WHITE, chess.E8)
True

>>> attackers = board.attackers(chess.WHITE, chess.F3)
>>> attackers
SquareSet(0b0000000000000000000000000000000000000000000000000100000001000000)
>>> chess.G2 in attackers
True
>>> print(attackers)
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . 1 .
. . . . . . 1 .

#######################################################################################################################
########################Parses and creates SAN representation of moves.################################################

>>> board = chess.Board()

>>> board.san(chess.Move(chess.E2, chess.E4))
'e4'

>>> board.parse_san('Nf3')
Move.from_uci('g1f3')

>>> board.variation_san([chess.Move.from_uci(m) for m in ["e2e4", "e7e5", "g1f3"]])
'1. e4 e5 2. Nf3'

#######################################################################################################################
#######################Parses and creates FENs, extended FENs and Shredder FENs.#######################################

>>> board.fen()
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
>>> board.shredder_fen()
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w HAha - 0 1'
>>> board = chess.Board("8/8/8/2k5/4K3/8/8/8 w - - 4 45")
>>> board.piece_at(chess.C5)
Piece.from_symbol('k')

########################################################################################################################
##########################################Parses and creates EPDs.######################################################

>>> board = chess.Board()
>>> board.epd(bm=board.parse_uci("d2d4"))
'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - bm d4;'

>>> ops = board.set_epd("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - bm Qd1+; id \"BK.01\";")
>>> ops == {'bm': [chess.Move.from_uci('d6d1')], 'id': 'BK.01'}
True

########################################################################################################################
############################Detects absolute pins and their directions.#################################################


########################################################################################################################
###################################Read Polyglot opening books. Docs.###################################################

>>> import chess.polyglot

>>> book = chess.polyglot.open_reader("data/polyglot/performance.bin")

>>> board = chess.Board()
>>> main_entry = book.find(board)
>>> main_entry.move()
Move.from_uci('e2e4')
>>> main_entry.weight
1
>>> main_entry.learn
0

>>> book.close()

########################################################################################################################
#############Read and write PGNs. Supports headers, comments, NAGs and a tree of variations. Docs.######################

>>> import chess.pgn

>>> pgn = open("data/pgn/molinari-bordais-1979.pgn")
>>> first_game = chess.pgn.read_game(pgn)
>>> pgn.close()

>>> first_game.headers["White"]
'Molinari'
>>> first_game.headers["Black"]
'Bordais'

>>> # Get the mainline as a list of moves.
>>> moves = first_game.main_line()
>>> first_game.board().variation_san(moves)
'1. e4 c5 2. c4 Nc6 3. Ne2 Nf6 4. Nbc3 Nb4 5. g3 Nd3#'

>>> # Iterate through the mainline of this embarrasingly short game.
>>> node = first_game
>>> while not node.is_end():
...     next_node = node.variation(0)
...     print(node.board().san(next_node.move))
...     node = next_node
e4
c5
c4
Nc6
Ne2
Nf6
Nbc3
Nb4
g3
Nd3#

>>> first_game.headers["Result"]
'0-1'



########################################################################################################################
Probe Gaviota endgame tablebases (DTM, WDL). Docs.


########################################################################################################################
Probe Syzygy endgame tablebases (DTZ, WDL). Docs.

>>> import chess.syzygy

>>> tablebases = chess.syzygy.open_tablebases("data/syzygy/regular")

>>> # Black to move is losing in 53 half moves (distance to zero) in this
>>> # KNBvK endgame.
>>> board = chess.Board("8/2K5/4B3/3N4/8/8/4k3/8 b - - 0 1")
>>> tablebases.probe_dtz(board)
-53

>>> tablebases.close()

########################################################################################################################
####################################Communicate with an UCI engine. Docs.###############################################

>>> import chess.uci

>>> engine = chess.uci.popen_engine("stockfish")
>>> engine.uci()
>>> engine.author  # doctest: +SKIP
'Tord Romstad, Marco Costalba and Joona Kiiski'

>>> # Synchronous mode.
>>> board = chess.Board("1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1")
>>> engine.position(board)
>>> engine.go(movetime=2000)  # Gets tuple of bestmove and ponder move.
BestMove(bestmove=Move.from_uci('d6d1'), ponder=Move.from_uci('c1d1'))

>>> # Asynchronous mode.
>>> def callback(command):
...    bestmove, ponder = command.result()
...    assert bestmove == chess.Move.from_uci('d6d1')
...
>>> command = engine.go(movetime=2000, async_callback=callback)
>>> command.done()
False
>>> command.result()
BestMove(bestmove=Move.from_uci('d6d1'), ponder=Move.from_uci('c1d1'))
>>> command.done()
True

>>> # Quit.
>>> engine.quit()
0

'''