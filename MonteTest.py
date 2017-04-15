
import GetBoardString as GBS
import chess
import Monte2 as Monte

b = chess.Board()
gbs = GBS.GetBoardString().get_BoardString(b)
b_str = gbs
mt = Monte.Monte(b_str)

p = mt.predict()