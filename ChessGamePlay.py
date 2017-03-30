#체스게임 플레이

import chess
import MontecarloTreeSearch as AI # 몬테칼로
import MakeLegalMoves as MLM # legal_moves 변환

MaxGameNum = 100
boardList = [0 * 1 for i in range(100)]
CountGame = 0

class AI: # 체스 AI 클래스
    def __init__(self):
        return



class chessGame:
    def __init__(self):
        self.MainBoard = chess.Board()
        self.Mode = 0  # 1. AI모드 2. 2인 대전모드 3. 네트워크모드
        self.PlayerTurn = True  # AI모드이거나 네트워크모드일때만 고려, True = White , False = Black

    def make_board(self):  # 새로운 보드를 하나 생성
            self.MainBoard = chess.Board() # mainBoard 체스 게임 생성

    def push_san(self, cmd):  # San 기보 수 입력
        self.MainBoard.push_san(cmd)

    def select_mode(self): # 모드를 선택
        print("모드를 선택하십시오.")
        print("1. 싱글-AI대전")
        print("2. 2인 대전")
        print("3. 네트워크대전")

        self.Mode = int(input("선택할 모드를 입력해주세요 : "))

        selection = False
        while (not selection):
            if (self.Mode == 1):
                print("AI 대전을 시작합니다.")
                selection = True
            elif (self.Mode == 2):
                print("2인대전을 시작합니다.")
                selection = True
            elif (self.Mode == 3):
                print("네트워크대전을 시작합니다.")
                selection = True
            else:
                print("지원하는 모드가 아닙니다.")
                return

    def select_turn(self): # 싱글 대전일때만, 모드를 선택
        print("플레이할 색상을 선택하세요. 흰색이 선입니다.")

        flag = int(input("1. White  2.Black :"))

        if(flag == 1):
            self.PlayerTurn = True
        else:
            self.PlayerTurn = False

    def play_game(self) : # 게임 플레이를 동작
        self.make_board() # 게임을 생성하고
        self.select_mode()
        self.play_board()

    def play_board(self):


        while(not self.MainBoard.is_game_over()) :
            self.display_board()
            self.print_legalmoves()
            
            # AI 대전 모드
            if(self.Mode == 1):
                if(self.PlayerTurn == self.turn_board()):
                    if(self.PlayerTurn):
                        print("흰 말")
                    else:
                        print("검은 말")
                    cmd = input("수 입력 : ")
                else:
                    ai = AI.Monte()
                    cmd = ai.asking(self.MainBoard) # AI한테 질문~

            # 2인 대전 모드
            elif(self.Mode == 2) :
                if(self.turn_board()):
                    cmd = input("흰말 : ")
                else:
                    cmd = input("검정말 : ")

            # 네트워크 대전 모드
            elif(self.Mode ==3) :
                print("네트워크모드는 아직 구성되지 않았습니다. 2인대전모드로 전환합니다.")
                if(self.turn_board()):
                    cmd = input("흰말 : ")
                else:
                    cmd = input("검정말 : ")
                    
            print("------------------------")

            self.MainBoard.push_san(cmd)

            # 룰 체크
            self.check_rules()

    def display_board(self):
        print("------------------------")
        print(self.MainBoard)

    def print_legalmoves(self):
        MM = MLM.MovesMaker()
        moves = str(self.MainBoard.legal_moves)
        move_arr = MM.make(moves)
        print("가능한 수 목록 : ",move_arr)

    '''보드상태 배열로 나눠 받기'''
    def parse_board(self):
        temp = self.MainBoard
        temp2 = temp[7:-15].split("/")
        return temp2

    '''보드판 출력할 때, 좌표계도 같이 출력'''
    def display_coordinate(self):
        return

    def turn_board(self): # 현재 보드의 턴을 알려줌
        return self.MainBoard.turn

    def check_rules(self): # 전체 룰을 체크
        return

    def check_draw(self): # 무승부 룰 체크
        return

    def check_end(self): # 게임 오버 룰 체크
        return



    #############################
    ###### 단 순 U I  구성 ######
    def UI_Intro(self) :
        print("WelCome DeepPurple")

    def UI_start(self) :
        print("Press any Key to continue")

    ###### 단 순 U I  구성 ######
    #############################



# 소스 구동

game = chessGame()

game.play_game()