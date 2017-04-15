import chess.pgn
import chess
import numpy
import random
import Board2Array as BA
import MakeLegalMoves as MLM

'''
사용법 : 

# 폴더경로를 이용해 rd객체 하나를 생성
rd = pgn_reader('./test/test.pgn')

# get_data()메소드를 이용하면, index 몇번쨰 수인지, input 보드상태, output 명령어, r 승패결과
index, input, output, r = rd.get_data() 
'''

def read_games(f): # pgn파일을 불러와 한 게임 별로 배열로 만들어 리턴함
    gs = []
    while True:
        try:
            g = chess.pgn.read_game(f)
            gs.append(g) # 현재 포인터가 가르키는 게임을 리턴하고 다음 게임으로 포인터 이동
        except KeyboardInterrupt:
            raise
        except:
            continue

        if not g:
            break
    gs.pop()
    return gs

class pgn_reader:
    def __init__(self,filename=None):
        self.gs = []
        self.len = 0
        self.filename = filename
        self.load_games()

    def set_pgn(self,filename):
        self.filename = filename

    def load_games(self):
        f = open(self.filename)
        self.gs = read_games(f)
        self.len = len(self.gs)

    def print_games(self):
        for i in range(self.len):
            self.info_game(i)

    def info_game(self, n): # n번쨰 게임의 header 정보 리턴
        if(n >= self.len):
            return
        print(self.gs[n].headers)

    def get_game(self, g):
        gns = []
        gn = g.end()
        move_num = 0
        while gn:
            gns.append((move_num, gn, gn.board().turn))
            move_num += 1
            gn = gn.parent

        result=g.headers['Result']
        return gns, result

    def analyze(self, last = False):
        index=[]
        pboard=[]
        board=[]
        rboard=[]
        results = []
        ba = BA.Board2Array()
        for i in range(self.len):
            gns, result = self.get_game(self.gs[i])
            if len(gns) < 2:
                continue
            print(len(gns)-1)
            rand = random.randint(1,len(gns)-1)
            parent = gns[rand][1].board()
            move = gns[rand - 1][1].move

            child = parent.copy()
            rchild = parent.copy()

            child.push(move)

            # random child move
            lm = parent.legal_moves
            mlm = MLM.MovesMaker()
            mlm.make(lm.__str__())
            rmove_san = mlm.get_RandomMove()
            rchild.push_san(rmove_san.__str__())

            # # board2array :
            child = ba.board2array(child)  # b2array(b, flip)
            rchild = ba.board2array(rchild)

            # list append
            index.append(len(gns) - rand)
            board.append(child)
            rboard.append(rchild)
            results.append(result)
            pboard.append(parent)

        return index,pboard, board, rboard, results

    def trans(self, index, pboard, board, rboard, result):
        rm = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}  # 게임의 끝, ( 백승 = 1, 흑승 = -1, 무승부, 0 )
        results= []
        for i in result:
            results.append(rm[i])
        return index,pboard, board, rboard, results

    def get_data(self, last = False):
        index, pboard, board, rboard, results = self.analyze(last)
        temp = self.trans(index,pboard, board, rboard, results)
        return temp