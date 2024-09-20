# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 구슬판 기울이는 함수
def Move(rX, rY, bX, bY, i):
    # 초기값 선언
    rStuck, bStuck = False, False

    # 둘다 멈출때까지 반복
    while not rStuck or not bStuck:
        rX_, rY_, bX_, bY_ = rX+dx[i], rY+dy[i], bX+dx[i], bY+dy[i]

        # 구슬이 게임판에서 이동 가능한지 확인
        if not rStuck:
            if Map[rX_][rY_] == '#': rStuck = True
            if Map[rX_][rY_] == 'O':
                rStuck = True
                rX, rY = rX_, rY_
        
        if not bStuck:
            if Map[bX_][bY_] == '#': bStuck = True
            if Map[bX_][bY_] == 'O':
                bStuck = True
                bX, bY = bX_, bY_
        
        # 게임판에 의해 가로막힌 다른 구슬이 막는지 확인
        if not rStuck and bStuck and rX_ == bX and rY_ == bY: rStuck = True
        if not bStuck and rStuck and bX_ == rX and bY_ == rY: bStuck = True

        # 구슬이 멈추지 않음
        if not rStuck: rX, rY = rX_, rY_
        if not bStuck: bX, bY = bX_, bY_
    
    return rX, rY, bX, bY

# 구슬 및 구멍 위치 찾기
rX, rY, bX, bY, hX, hY = 0, 0, 0, 0, 0, 0
for x in range(N):
    for y in range(M):
        if Map[x][y] == 'R': rX, rY = x, y
        if Map[x][y] == 'B': bX, bY = x, y
        if Map[x][y] == 'O': hX, hY = x, y

# 초기값 선언
result = -1
queue = deque([(rX, rY, bX, bY, 0)])
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[rX][rY][bX][bY] = True

# BFS
while queue:
    rX, rY, bX, bY, count = queue.popleft()

    # 도착
    if bX == hX and bY == hY: continue # 파란 구슬이 나와버림
    if rX == hX and rY == hY: # 빨간 구슬 탈출
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        rX_, rY_, bX_, bY_ = Move(rX, rY, bX, bY, i)

        # 탐색 불가 조건
        if visited[rX_][rY_][bX_][bY_]: continue

        # 탐색
        visited[rX_][rY_][bX_][bY_] = True

        # 다음 탐색
        queue.append((rX_, rY_, bX_, bY_, count+1))

# 출력부
print(result)