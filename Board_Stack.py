import chess


class Board_Stack():
    def __init__(self):
        self.main_board = chess.Board
        self.BoardStack = []
        self.temp_board = chess.Board


    def set_mainBoard(self, inputBoard):
        self.main_board = inputBoard.copy()

    def stack_push(self, command):
        self.BoardStack.append(command)

    def stack_pop(self):
        return self.BoardStack.pop(0) # ????

    def is_emptyStack(self):

        return #bool type

    def clear_Stack(self):
        self.BoardStack.clear()

    def display_Board(self, board):
        print(board)

