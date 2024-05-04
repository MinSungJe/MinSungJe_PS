# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]

# 위치 찾기
rPos, bPos, oPos = [0, 0], [0, 0], [0, 0]
for i in range(N):
    for j in range(M):
        if Map[i][j] == 'R': rPos[0], rPos[1] = i, j
        if Map[i][j] == 'B': bPos[0], bPos[1] = i, j
        if Map[i][j] == 'O': oPos[0], oPos[1] = i, j

# 보드 움직이는 함수
def Move(X1, Y1, X2, Y2, d):
    rX, rY, bX, bY = X1, Y1, X2, Y2

    rStop, bStop = False, False
    while True: # 두 구슬이 멈출때까지 이동
        rX_, rY_, bX_, bY_ = rX+dx[d], rY+dy[d], bX+dx[d], bY+dy[d]

        # 구슬 멈추는 조건
        if Map[rX_][rY_] == '#': rStop = True
        if Map[bX_][bY_] == '#': bStop = True
        if Map[rX_][rY_] == 'O':
            rX, rY = rX_, rY_
            rStop = True
        if Map[bX_][bY_] == 'O':
            bX, bY = bX_, bY_
            bStop = True
        if bStop and rX_ == bX and rY_ == bY: rStop = True
        if rStop and bX_ == rX and bY_ == rY: bStop = True

        # 적용
        if rStop and bStop: break
        if not rStop: rX, rY = rX_, rY_
        if not bStop: bX, bY = bX_, bY_
    
    return rX, rY, bX, bY

# BFS
queue = deque([(rPos[0], rPos[1], bPos[0], bPos[1], 0)])
while queue:
    rX, rY, bX, bY, count = queue.popleft()

    # 탐색 불가 조건
    if visited[rX][rY][bX][bY]: continue
    if count > 10: break

    # 탐색
    visited[rX][rY][bX][bY] = True
    if bX == oPos[0] and bY == oPos[1]: # 파란 구슬 도착(먼저 확인)
        continue
    if rX == oPos[0] and rY == oPos[1]: # 빨간 구슬 도착
        result = 1
        break

    # 다음 탐색
    for i in range(4):
        rX_, rY_, bX_, bY_ = Move(rX, rY, bX, bY, i)
        queue.append((rX_, rY_, bX_, bY_, count+1))

# 출력부
print(result)