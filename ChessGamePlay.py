#체스게임 플레이

import chess
import MontecarloTreeSearch as Monte

board = chess.Board()

def startBoard():
    board = chess.Board()

def push(str):
    board.push_san(str)

startBoard()

while(True):
    print(board)

    #print(board.turn) # true 는 white false 는 black
    if (board.turn):
        choice = input("white choice ( exit = 0 ) : ")
    else :
        choice = input("black choice ( exit = 0 ) : ")

    if (choice == 0) :
        break
    else :
        board.push_san(choice)#
