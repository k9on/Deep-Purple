import numpy
class Board2Array:

    def board2array(self, chessBoard):
        str = chessBoard.__str__()
        str = str.replace('\n', ' ')
        str = str.replace(' ','')
        boardArray = []
        #boardArray = numpy.zeros(64, dtype=numpy.float32) # 초기화

        for i in range(len(str)):
            boardArray.append(-1)

        #---------백-------\--------흑-----------빈칸
        # 0  1  2  3  4  5  6  7  8  9  10  11  12
        # 킹 퀸 말  숍 폰 룩 킹  퀸 말 숍  폰  룩  빈칸
        for i in range(len(str)):
            if str[i] ==   'K': boardArray[i] = [1,0,0,0,0,0,0,0,0,0,0,0,0]
            elif str[i] == 'Q': boardArray[i] = [0,1,0,0,0,0,0,0,0,0,0,0,0]
            elif str[i] == 'N': boardArray[i] = [0,0,1,0,0,0,0,0,0,0,0,0,0]
            elif str[i] == 'B': boardArray[i] = [0,0,0,1,0,0,0,0,0,0,0,0,0]
            elif str[i] == 'P': boardArray[i] = [0,0,0,0,1,0,0,0,0,0,0,0,0]
            elif str[i] == 'R': boardArray[i] = [0,0,0,0,0,1,0,0,0,0,0,0,0]
            elif str[i] == 'k': boardArray[i] = [0,0,0,0,0,0,1,0,0,0,0,0,0]
            elif str[i] == 'q': boardArray[i] = [0,0,0,0,0,0,0,1,0,0,0,0,0]
            elif str[i] == 'n': boardArray[i] = [0,0,0,0,0,0,0,0,1,0,0,0,0]
            elif str[i] == 'b': boardArray[i] = [0,0,0,0,0,0,0,0,0,1,0,0,0]
            elif str[i] == 'p': boardArray[i] = [0,0,0,0,0,0,0,0,0,0,1,0,0]
            elif str[i] == 'r': boardArray[i] = [0,0,0,0,0,0,0,0,0,0,0,1,0]
            elif str[i] == '.': boardArray[i] = [0,0,0,0,0,0,0,0,0,0,0,0,1]

        return boardArray



    # 명령어 str(e3e4) -> int(5354) 로 만들기 위한 함수
    def replace(self,char):
        if char == "a":
            return "1"
        elif char == "b":
            return "2"
        elif char == "c":
            return "3"
        elif char == "d":
            return "4"
        elif char == "e":
            return "5"
        elif char == "f":
            return "6"
        elif char == "g":
            return "7"
        elif char == "h":
            return "8"

    def remake(self,output):
        output_len = len(output)
        output2 = []

        for i in range(output_len):
            temp = numpy.zeros(4, dtype=numpy.float32)
            temp[0] = int(self.replace(output[i][0]))
            temp[1] = int(output[i][1])
            temp[2] = int(self.replace(output[i][2]))
            temp[3] = int(output[i][3])

            output2.append(temp)
        return output2
    
    # 8x8*13형태로

    def trans_result(self,result):
        rm = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}  # 게임의 끝, ( 백승 = 1, 흑승 = -1, 무승부, 0 )

        return rm[result]