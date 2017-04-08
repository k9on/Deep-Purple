import chess.pgn
import numpy
import random
import Board2Array as BA

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

        if not g: # 현재 포인터가 비어 있으면 yield 중지
            break
    gs.pop()
    #print("Num of Games in The file : ",len(gs))
    return gs # yield 는 한방에 return 하지 않고 배열로 하나하나 추가 해놓고 다 끝나면 통째로 리턴

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
    def info_game(self, n):
        if(n >= self.len):
            return
        print(self.gs[n].headers)

    def get_game(self, g):
        gns = []
        result = ""
        gn = g.end()
        move_num = 0
        headers = g.headers
        while gn:
            gns.append((move_num, gn, gn.board().turn))

            move_num += 1
            gn = gn.parent
        #
        # for i in range(len(gns)):
        #     print(gns[i][1].board())
        #     print(gns[i-1][1].move)
        result=g.headers['Result']
        return gns, result

    def analyze(self, last = False):
        index=[]
        input=[]
        output=[]
        results = []
        ba = BA.Board2Array()
        for i in range(self.len):
            gns, result = self.get_game(self.gs[i])
            #print(result)
            flag = 1
            if last:
                flag = 0
            rand = random.randint(flag,len(gns)-1)
            b = gns[rand][1].board()
            b = ba.board2array(b)
            board = b # b2array(b, flip)
            move = gns[rand-1][1].move
            input.append(board)
            move_str = move.__str__()
            #print(move_str)
            output.append(move_str)
            results.append(result)
            index.append(len(gns)-rand)
        return index, input, output, results

    def get_data(self, last = False):
        index, input, output, results = self.analyze(last)
        temp = self.trans(index, input, output, results)
        return temp



    def trans(self,index,input,output,results):
        rm = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}  # 게임의 끝, ( 백승 = 1, 흑승 = -1, 무승부, 0 )
        result= []
        boards = []
        for i in results:
            result.append(rm[i])
        ba = BA.Board2Array()
        output = ba.remake(output)
        return index, input,output,result
