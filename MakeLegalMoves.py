class MovesMaker:
    def make(self, str):
        start = str.find("(") # ( 이 시작하는 위치 반환
        mid = str[start+1:-2] # ( 의 다음 위치 부터 마지막 -2 까지 반환
        temp = mid.split(",") #

        return temp

