import chess


class Board_Stack():
    def __init__(self, boardString = None): #boardString은 Tree 생성할때 전달 받는 String
        self.boardStack =[]
        if boardString == None: #boardString이 None이면 chessBoard가 전부 빈칸
            self.chessBoard = chess.Board()
        else:
            self.chessBoard = chess.Board(boardString)

    def stack_push(self, command): #boardStack에 체스판 쌓기
        self.chessBoard.push_san(command) #입력 받은 명령어를 chessBoard에 갱신
        self.boardStack.append(command)

    def stack_pop(self): #boardStack의 선입선출
        self.chessBoard.pop() #가장 최근 들어간 명령어를 pop
        return self.boardStack.pop() # pop() 괄호 안에 인자의 디폴트는 0이며, 정수를 넣으면 배열의 인덱스로 취급

    def all_push_one(self, commands): # commands 배열을 받으면 한번에 다 넣기
        self.clear_Stack() # 푸쉬 하기전에 일단 비우고
        
        while(len(commands) != 0): # 다 넣기
            self.stack_push(commands.pop())

    def is_emptyStack(self): #boardStack이 비었으면 True, 아니면 False

        if self.boardStack == None :
            return True
        else:
            return False

    def clear_Stack(self): # boardStack 비우기
        self.boardStack.clear()

    def display_Board(self): #boardStack에 입력된 명령어까지 체스판으로 출력
        print(self.chessBoard)

    def get_ChessBoard(self):
        return self.chessBoard
    def get_GameOver(self):
        return self.chessBoard.is_game_over()
    def get_Result(self):
        return self.chessBoard.result()
    def get_Color(self):
        #current노드의 현재 말 색깔을 알기 위해
        #turn이  True : White , False : Black
        return self.chessBoard.turn


