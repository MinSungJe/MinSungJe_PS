# 빠른 입력 및 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
result = [0,0]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = (-1,1,0,0)
dy = (0,0,-1,1)

# BFS
def BFS(x,y,c,cS):
    # BFS 준비
    queue = deque()
    queue.append((x,y,c,cS))

    # 비재귀 DFS
    while queue:
        X, Y, color, canSee = queue.popleft()

        # 탐색 불가 조건
        # 1. 탐색하려는 위치가 N*N을 넘어선 경우
        if X < 0 or X >= N or Y < 0 or Y >= N: continue

        # 2. 색약인 경우와 색약이 아닌 경우로 나뉨
        if canSee: # 색약이 아닌경우
            if Map[X][Y] != color: continue # 탐색하려는 위치가 다른 색깔인 경우
        else: # 색약인 경우
            if color == 'B': # color가 파랑인 경우 -> 탐색하는 위치가 파란색이 아닌 경우
                if Map[X][Y] != 'B': continue
            else: # color가 파랑이 아닌 경우 -> 탐색하는 위치가 파란색인 경우
                if Map[X][Y] == 'B': continue
        
        # 3. 이미 탐색한 적이 있는 위치인 경우
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True

        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queue.append((X_,Y_,color,canSee))

# 색약이 아닌 경우 시작점 지정
for i in range(N):
    for j in range(N):
        # 빨간색을 보는 눈
        if Map[i][j] == 'R' and not visited[i][j]:
            result[0] += 1
            BFS(i,j,'R',True)
        # 초록색을 보는 눈
        if Map[i][j] == 'G' and not visited[i][j]:
            result[0] += 1
            BFS(i,j,'G',True)
        # 파란색을 보는 눈
        if Map[i][j] == 'B' and not visited[i][j]:
            result[0] += 1
            BFS(i,j,'B',True)

# 초기값 초기화
visited = [[False for _ in range(N)] for _ in range(N)]

# 색약인 경우 시작점 지정
for i in range(N):
    for j in range(N):
        # 빨간색을 보는 눈
        if Map[i][j] == 'R' and not visited[i][j]:
            result[1] += 1
            BFS(i,j,'R',False)
        # 초록색을 보는 눈
        if Map[i][j] == 'G' and not visited[i][j]:
            result[1] += 1
            BFS(i,j,'G',False)
        # 파란색을 보는 눈
        if Map[i][j] == 'B' and not visited[i][j]:
            result[1] += 1
            BFS(i,j,'B',False)

print(*result)