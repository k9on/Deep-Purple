#체스게임 플레이

import chess
import MontecarloTreeSearch as Monte

MaxGameNum = 100
boardList = [0 * 1 for i in range(100)]
CountGame = 0
MainBoard = chess.Board()

def NewBoard():
    if(CountGame== MaxGameNum):
        print("플레이 가능한 횟수를 초과하엿습니다.")
    else:
        boardList[CountGame] = chess.Board()
        MainBoard = boardList[CountGame]
        Countgame = counting(CountGame)

def counting(count) :
    return count + 1

def push(str):
    MainBoard.push_san(str)

def UI_Intro() :
    print("WelCome DeepPurple")

def UI_start() :
    print("Press any Key to continue")

def play() :
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


# 소스 구동

NewBoard()
play()