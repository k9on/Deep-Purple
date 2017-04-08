import numpy
class Board2Array:

    def board2array(self, chessBoard):
        str = chessBoard.__str__()
        str = str.replace('\n', ' ')
        str = str.replace(' ','')
        boardArray = []
        boardArray = numpy.zeros(64, dtype=numpy.int8) # 초기화

        #for i in range(len(str)):
        #    boardArray.append(-1)

        for i in range(len(str)):
            if str[i] == 'K': boardArray[i] = 1
            elif str[i] == 'Q': boardArray[i] = 2
            elif str[i] == 'N': boardArray[i] = 3
            elif str[i] == 'B': boardArray[i] = 4
            elif str[i] == 'P': boardArray[i] = 5
            elif str[i] == 'R': boardArray[i] = 6
            elif str[i] == 'k': boardArray[i] = 7
            elif str[i] == 'q': boardArray[i] = 8
            elif str[i] == 'n': boardArray[i] = 9
            elif str[i] == 'b': boardArray[i] = 10
            elif str[i] == 'p': boardArray[i] = 11
            elif str[i] == 'r': boardArray[i] = 12
            #elif str[i] == '.': boardArray[i] = 0 # 원래 0으로 초기화해서 없앰

        return boardArray
