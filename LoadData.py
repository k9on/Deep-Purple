import chess.pgn
import numpy
import random


def bb2array(b, flip=False):  # b - board를 배열로 변환
    x = numpy.zeros(64, dtype=numpy.int8)  # 하나의 체스 상황을 담아둘 8x8 배열을 만들어 둠
    p=b.pieces
    print(p)
    #
    # for pos, piece in enumerate(b.pieces):  # 2차원 배열 [ 인덱스 / 체스말 번호 ]
    #     if piece != 0:  # 체스말이 없는 빈칸이 아니면
    #         color = int(bool(b.occupied_co[chess.BLACK] & chess.BB_SQUARES[pos]))  # 0 or 1 말이 흑인지 백인지
    #         col = int(pos % 8)  # 64개의 인덱스를 8로 나눠 열을 구함
    #         row = int(pos / 8)  # 64개의 인덱스를 8로 나눠 행을 구함
    #         if flip:  # flip이 True면 상황을 반전 시켜서 출력함
    #             row = 7 - row  # 뒤집기
    #             color = 1 - color  # 뒤집기
    #
    #         piece = color * 7 + piece  # 백은 0~6 흑은 7~13
    #
    #         x[row * 8 + col] = piece  # 행열로 된 상태를 1차원 배열로 다시 만듬

    return x  # 리턴

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
        for i in range(self.len):
            gns, result = self.get_game(self.gs[i])
            #print(result)
            flag = 1
            if last:
                flag = 0
            rand = random.randint(flag,len(gns)-1)
            b = gns[rand][1].board()
            board = bb2array(b)
            move = gns[rand-1][1].move
            input.append(board)
            output.append(move)
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

        return index, input,output,result



rd = pgn_reader('./test/test.pgn')
index, input, output, r = rd.get_data()
print(index)
print(input)
print(output)
print(r)

# def parse_game(g):  # g는 1개 단위의 게임기보

#     gn = g.end()  # gn(Game Node) 게임의 끝
#     if not gn.board().is_game_over():  # 마지막 기보가 게임이 끝난 기보 상태가 아니면 리턴, 즉 기보 데이터의 손상 혹은 기권을 의미
#         return None
#     gns = []  # 게임 노드들을 담아둘 배열
#     moves_left = 0
#     while gn:  # 게임의 노드가 끝날 때 까지
#         gns.append((moves_left, gn, gn.board().turn == 0))  # 게임 노드를 계속해서 배열화, 몇번째 착수 인지,
#         gn = gn.parent
#         moves_left += 1
#
#     print
#     len(gns)
#     if len(gns) < 10:  # 게임기보를 마지막부터 처음까지 배열화하였는데, 배열수가 10개 이하면 마지막 기보상태를 출력
#         print
#         g.end()
#
#     gns.pop()  # 마지막에 넣은게 pop, 즉 게임시작 기보는 pop으로 제거
#
#     moves_left, gn, flip = random.choice(gns)  # remove first position
#     # gns에 넣었던 노드중에 랜덤으로 하나 뽑음
#
#     b = gn.board()  # 보드
#     x = bb2array(b, flip=flip)  # 보드상태 64개 배열로
#     b_parent = gn.parent.board()  # 부모노드
#     x_parent = bb2array(b_parent, flip=(not flip))  # 부모노드의 보드상태
#     if flip:  # 적이면
#         y = -y  # Switch
#
#     # generate a random baord
#     moves = list(b_parent.legal_moves)  # 부모노드의 moves
#     move = random.choice(moves)  # 랜덤을 하나 뽑아서
#     b_parent.push(move)  # 부모노드에 적용
#     x_random = bb2array(b_parent, flip=flip)  # 배열화
#
#     if moves_left < 3:  # 끝에서 세번째정도면
#         print
#         moves_left, 'moves left'
#         print
#         'winner:', y
#         print
#         g.headers
#         print
#         b
#         print
#         'checkmate:', g.end().board().is_checkmate()
#     return (x, x_parent, x_random, moves_left, y)
