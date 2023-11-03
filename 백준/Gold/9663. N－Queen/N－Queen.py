# 입력부
N = int(input())

# 초기값 선언
Map = [[0 for _ in range(N)] for _ in range(N)]
result = 0
dx = (1, 1, 1)
dy = (0, -1, 1)

# 함수 선언
def NQueen(x):
    global result, Map
    
    # 체스판 한 줄 내에 놓을 수 있는 곳 확인
    for y in range(N):
        if not Map[x][y]:
            if x == N-1: # 마지막 줄이면 결과에 추가
                result += 1
                return
            setMap(x, y, 1) # 놓을 수 없는 곳 최신화
            NQueen(x+1)
            setMap(x, y, -1) # backtracking

# Map 배열을 수정하는 함수
def setMap(X, Y, bool):
    global Map
    for i in range(3):
        for n in range(N):
            X_ = X + (dx[i] * n)
            Y_ = Y + (dy[i] * n)
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: break
            Map[X_][Y_] += bool
    

# 실행 및 출력
NQueen(0)
print(result)