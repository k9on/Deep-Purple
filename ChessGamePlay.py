#체스게임 플레이

import chess
import MontecarloTreeSearch as MCTS
import GetBoardString as GBS
import Monte2 as M
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
    monte = M.Monte()
    while(True):
        print("a b c d e f g h")
        print("---------------")
        print(MainBoard,chr(13))
        print("---------------")
        print("a b c d e f g h")

        #print(board.turn) # true 는 white false 는 black
        if (MainBoard.turn):
            flag = True
            while flag:
                print(MainBoard.legal_moves)
                choice = input("choice:")
                if choice != 0:
                    tmpBoard = MainBoard.copy()
                    try:
                        tmpBoard.push_san(choice)
                        flag = False
                    except ValueError:
                        print("다시 선택해주세요")

        else :
            gbs = GBS.GetBoardString().get_BoardString(MainBoard)
            monte.set_state(gbs, MainBoard.turn)
            choice = monte.predict()

        if (choice == "0") :
            print("bye")
            break
        else :
            print("\r")
            MainBoard.push_san(choice)


# 소스 구동

NewBoard()
play()
