# 빠른 입력 및 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
n, m = map(int, input().split())
Map = [list(map(int,input().split())) for _ in range(n)]

# 초기값 선언
result = [[-1 for _ in range(m)] for _ in range(n)] # 결과 배열
dx = (-1,1,0,0)
dy = (0,0,-1,1)
# BFS
def BFS(x,y):
    global result
    # 초기값 선언
    queue = deque() # BFS를 위한 queue
    queue.append((x,y,0))

    # BFS 시작
    while queue:
        X, Y, count = queue.popleft()
        
        # 탐색 불가 조건
        # 1. 탐색하려는 위치가 좌표를 넘어섬
        if X < 0 or X >= n or Y < 0 or Y >= m: continue
        # 2. 탐색하려는 위치가 갈 수 없는 곳임
        if Map[X][Y] == 0: continue
        # 3. 탐색하려는 위치는 이미 간 곳임
        if result[X][Y] > -1: continue

        # 탐색 및 결과값 수정
        result[X][Y] = count

        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queue.append((X_,Y_,count+1))

# 시작점 탐색
for i in range(n):
    for j in range(m):
        if Map[i][j] == 0: result[i][j] = 0
        if Map[i][j] == 2: BFS(i,j)

# 출력부
for i in range(n):
    print(*result[i])