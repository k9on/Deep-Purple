#체스게임 플레이

import chess
import MontecarloTreeSearch as AI

MaxGameNum = 100
boardList = [0 * 1 for i in range(100)]
CountGame = 0
MainBoard = chess.Board()
Mode = False # << 인공지능 모드 유무
AI_color = False # << 인공지능 흑백 여부 백 True

def NewBoard(): # 새로운 보드를 하나 생성
    if(CountGame== MaxGameNum): # 최대 수를 초과하면 문구 출력 후 escape
        print("플레이 가능한 횟수를 초과하엿습니다.") # 경고 문구
    else: # 보드 생성
        boardList[CountGame] = chess.Board() # 리스트에 보드를 생성하고
        MainBoard = boardList[CountGame] # main 보드로 갱신
        Countgame = counting(CountGame) # 게임수 카운팅

def counting(count) : # 게임 보드수 카운트 최대 MaxGameNum 까지
    return count + 1 # 하나씩 ++

def push(str): # 수 입력
    MainBoard.push_san(str)

def selectMode():
    print("AI 대전모드 인지 선택")
    print("AI의 흑백 선택")

def play() : # 게임 모드에 따라 유동적으로 작동해야함 # 수정해야함
    while(True):
        print(MainBoard)

        #print(board.turn) # true 는 white false 는 black
        if (MainBoard.turn):
            choice = input("white choice ( exit = 0 ) : ")
        else :
            choice = input("black choice ( exit = 0 ) : ")

        if (choice == "0") :
            print("bye")
            break
        else :
            MainBoard.push_san(choice)


#############################
###### 단 순 U I  구성 ######
def UI_Intro() :
    print("WelCome DeepPurple")

def UI_start() :
    print("Press any Key to continue")

###### 단 순 U I  구성 ######
#############################



# 소스 구동

NewBoard()
play()