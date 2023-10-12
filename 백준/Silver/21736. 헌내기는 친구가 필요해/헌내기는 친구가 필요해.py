# 빠른 입력 및 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
dx = (-1,1,0,0)
dy = (0,0,-1,1)
visited = [[False for _ in range(M)] for _ in range(N)]
result = 0
queue = deque()

# 도연이의 위치에서 시작
for i in range(N):
    for j in range(M):
        if Map[i][j] == 'I': queue.append((i,j))

# BFS
while queue:
    X, Y = queue.popleft()

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]

        # 탐색 불가 조건
        # 1. 탐색하려는 위치가 범위를 벗어남
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        # 2. 탐색하려는 위치는 벽임
        if Map[X_][Y_] == 'X': continue
        # 3. 탐색하려는 위치는 이미 방문한 적 있음
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True
        if Map[X_][Y_] == 'P': result += 1

        # 다음 queue 넣기
        queue.append((X_, Y_))

# 출력부
print(result if result else "TT")