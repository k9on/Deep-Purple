import chess


class Board_Stack():
    def __init__(self):
        self.main_board = chess.Board
        self.BoardStack = []
        self.temp_board = chess.Board


    def set_mainBoard(self, inputBoard): #boardStack변수를 갱신
        self.main_board = inputBoard.copy()

    def stack_push(self, command): #boardStack에 체스판 쌓기
        self.BoardStack.append(command)

    def stack_pop(self): #boardStack의 선입선출
        return self.BoardStack.pop(0) # ????

    def is_emptyStack(self): #boardStack이 비었으면 True, 아니면 False

        if self.BoardStack == None :
            return True
        else:
            return False

    def clear_Stack(self): # boardStack 비우기
        self.BoardStack.clear()

    def display_Board(self, board): #boardStack의 현재 체스판을 print로 출력
        print(board)

