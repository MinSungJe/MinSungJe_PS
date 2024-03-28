# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
token = [[deque() for _ in range(N)] for _ in range(N)]
info = list()
for i in range(K):
    X, Y, D = map(int, input().split())
    info.append([X-1, Y-1, D-1])
    token[X-1][Y-1].append(i)

# 초기값 선언
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

# 이동 함수
def act():
    for idx in range(K):
        X, Y, D = info[idx]
        X_, Y_ = X+dx[D], Y+dy[D]

        # 외부로 나가거나 파란색일때 한번 방향 바꾸기
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N or Map[X_][Y_] == 2:
            if D == 0 or D == 1: D = 1-D
            if D == 2 or D == 3: D = 5-D
            info[idx][2] = D
            X_, Y_ = X+dx[D], Y+dy[D]
        
        # 탐색 종료 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N or Map[X_][Y_] == 2: continue
        
        # 이동 준비
        temp = deque()
        length = len(token[X][Y])
        for i in range(length):
            if token[X][Y][i] == idx: tmpI = i
        for _ in range(tmpI, length): temp.append((token[X][Y].pop()))
        
        # 도착하려는 칸이 빨간색
        length = len(temp)
        for _ in range(length):
            if Map[X_][Y_] == 1: value = temp.popleft() # 빨간색인지 확인
            else: value = temp.pop()
            token[X_][Y_].append(value)
            info[value][0], info[value][1] = X_, Y_
        
        # 말이 4개 모였는지 확인
        if isGameOver(): return True
    
    return False

# 게임이 끝났는지 확인
def isGameOver():
    checkSheet = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(K):
        X, Y = info[i][0], info[i][1]
        checkSheet[X][Y] += 1
        if checkSheet[X][Y] >= 4: return True # 게임 끝

    return False

# 결과 도출 및 출력부
result = -1
count = 0
while count <= 1000:
    count += 1
    if act():
        result = count
        break
print(result)