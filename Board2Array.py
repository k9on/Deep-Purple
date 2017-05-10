import numpy as np
import chess

class Board2Array:

    def board2array(self, chessBoard):
        #chessBoard를 Model에 넣기 전에 원하는 input을 만들기 위한 함수

        str = chessBoard.__str__()
        str = str.replace('\n', ' ')
        str = str.replace(' ','')

        chessBoard.turn
        boardArray =[]
        #
        boardArray.append(self.piece2Number(str))
        boardArray.append(self.change2BlackAndWhite(str))
        boardArray.append(self.pieceFeature(str,'p'))
        boardArray.append(self.pieceFeature(str,'k'))
        boardArray.append(self.pieceFeature(str,'n'))
        boardArray.append(self.pieceFeature(str,'b'))
        boardArray.append(self.pieceFeature(str,'q'))
        boardArray.append(self.pieceFeature(str,'r'))
        boardArray.append(self.turnFeatrue(chessBoard,str))


        boardArray=self.transMyMatrix(boardArray)
        # boardArray = self.indexFeature(boardArray,index)
        return boardArray

    def piece2Number(self,str):
        #말을 숫자로 바꿔주는 함수
        boardArray = []
        for i in range(len(str)):
            if str[i] == 'K': boardArray.append(1)
            elif str[i] == 'Q': boardArray.append(2)
            elif str[i] == 'N': boardArray.append(3)
            elif str[i] == 'B': boardArray.append(4)
            elif str[i] == 'P': boardArray.append(5)
            elif str[i] == 'R': boardArray.append(6)
            elif str[i] == 'k': boardArray.append(7)
            elif str[i] == 'q': boardArray.append(8)
            elif str[i] == 'n': boardArray.append(9)
            elif str[i] == 'b': boardArray.append(10)
            elif str[i] == 'p': boardArray.append(11)
            elif str[i] == 'r': boardArray.append(12)
            elif str[i] == '.': boardArray.append(0)

        return boardArray

    def board2array2(self,chessBoard):
        if chessBoard.turn:
            turn = 1
        else:
            turn = 0
        str = chessBoard.__str__()
        str = str.replace('\n', ' ')
        str = str.replace(' ', '')
        boardArray = []
        # boardArray = numpy.zeros(64, dtype=numpy.float32) # 초기화

        for i in range(len(str)):
            boardArray.append(-1)

        # ---------백-------\--------흑-----------빈칸
        # 0  1  2  3  4  5  6  7  8  9  10  11  12
        # 킹 퀸 말  숍 폰 룩 킹  퀸 말 숍  폰  룩  빈칸
        for i in range(len(str)):
            if turn == 1:
                color = chess.WHITE
            else :
                color = chess.BLACK
            #
            # row = 8 - i // 8
            # col = 8 - i % 8
            # xy = row * 8 - col
            # attack =  chessBoard.is_attacked_by(turn,xy)
            # attack_value = 0
            # if attack :
            #     attack_value = 1
            # else :
            #     attack_value = 0
            #
            if str[i] == 'K':
                boardArray[i] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'Q':
                boardArray[i] = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'N':
                boardArray[i] = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'B':
                boardArray[i] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'P':
                boardArray[i] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'R':
                boardArray[i] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'k':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            elif str[i] == 'q':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
            elif str[i] == 'n':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
            elif str[i] == 'b':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
            elif str[i] == 'p':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
            elif str[i] == 'r':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
            elif str[i] == '.':
                boardArray[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            boardArray[i].append(turn)
        return boardArray
    def result2Onehot(self, results):
        None
    def change2BlackAndWhite(self, str):
        #보드를 말 색에따라 -1, 1로 변환
        colorBoard = []
        for i in str:
            if i.isupper():#대문자인경우 white
                colorBoard.append(1)
            elif i.islower(): #소문자인경우 black
                colorBoard.append(-1)
            else:
                colorBoard.append(0)

        return colorBoard
    def pieceFeature(self,str,piece):
        #폰, 폰의 색에 따라 -1 과 1로 반환
        #piece로 말의 종류를 입력 받아 종류에 따라 말의 특징을 가진 보드를 반환

        pieceLower=piece.lower()
        pieceUpper=piece.upper()

        featureBoard = []

        for i in str:
            if i == pieceLower or i == pieceUpper:
                if i.isupper(): #Piece가 대문자인 경우
                    featureBoard.append(1)
                elif i.islower():
                    featureBoard.append(-1)
            else:
                featureBoard.append(0)
        return featureBoard
    def addIndexFeature(self,boardArray, index): #몇번째 수인지 feature로 삽입
        for i in range(8):
            for j in range(8):
                boardArray[i][j].append(index)
        return boardArray
    def turnFeatrue(self, chessBoard, str):
        #chessBoard로 현재 턴을 받아 누구 차례인지 feature
        turn = chessBoard.turn # true면 백 false면 흑
        featureBoard = []

        for i in str:
            if turn == True: #현재 백의 차례일때 모두 1을 채운다
                if i.isupper():
                    featureBoard.append(1)
                else:
                    featureBoard.append(1)
            elif turn == False : # 흑의 차례일때 모두 0을 채운다
                if i.islower():
                    featureBoard.append(0)
                else:
                    featureBoard.append(0)

        return featureBoard
    def transMyMatrix(self, boardArray):
        #체스판 입력을 잘못 만들어
        #변환시켜주기 위한 임시 코드
        realBoard = [[[0]*9 for i in range(8)] for j in range(8)] #8x8x9배열 생성

        #boardArray는 (9,64)입력
        for k in range(9):
            for i in range(64):
                realBoard[int(i/8)][i%8][k]=boardArray[k][i]
        print
        return realBoard