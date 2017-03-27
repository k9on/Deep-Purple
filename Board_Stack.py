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

    def all_push_one(self, commands): # commands 배열을 받으면 한번에 다 넣기
        self.clear_Stack() # 푸쉬 하기전에 일단 비우고
        
        while(len(commands) != 0): # 다 넣기
            self.stack_push(commands.pop())
            
##############################################################################################################
############### 두 메소드 모두 스택을 소진하는 메소드로서 동시에 사용하면 안 됩니다 ##########################

    def realize_Board(self): # mainboard를 기준으로 stack을 참고하여 해당 보드를 구현
        self.temp_board = self.main_board.copy() # 메인보드의 손상을 막기 위해 temp화

        while(len(self.BoardStack)!=0): # 스택이 빌 때까지
            cmd = self.stack_pop() # 스택을 빼서
            self.temp_board.push_san(cmd) # 적용, commands를 구성할 때 legal_move에서 근거하였기 때문에
            # 올바르지 않은 명령어가 들어갈 경우는 없을 것이나, 예외처리를 할 필요성이 있는지 재고

        # 현재 보드상태 리턴
        return self.temp_board
     
    def get_legal_moves(self): # 현재 노드에서 합법적인 무브를 탐색
        self.realize_Board() # 무브탐색에 앞서 보드를 갱신
        moves = self.temp_board.legal_moves
        '''moves는 가능한 move로 구성된 str 배열이여야 하는데, legal_moves의 return 값이 그렇지 않으므로 전처리의 필요성이 잇음'''

############### 두 메소드 모두 스택을 소진하는 메소드로서 동시에 사용하면 안 됩니다 ##########################
###############################################################################################################

    def stack_pop(self): #boardStack의 선입선출
        return self.BoardStack.pop() # pop() 괄호 안에 인자의 디폴트는 0이며, 정수를 넣으면 배열의 인덱스로 취급

    def is_emptyStack(self): #boardStack이 비었으면 True, 아니면 False

        if self.BoardStack == None :
            return True
        else:
            return False

    def clear_Stack(self): # boardStack 비우기
        self.BoardStack.clear()

    def display_Board(self, board): #boardStack의 현재 체스판을 print로 출력
        print(board)

