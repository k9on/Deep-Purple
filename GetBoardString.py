import chess

class GetBoardString: #chess.Board()의 string을 만들기 위한 클래스
   def get_BoardString(self, board): #chess.Board를 board로 받음
        a1 = board.__repr__()
        c1 = a1[7:-2]
        #print(c1)
        #print(type(c1))
        return c1
