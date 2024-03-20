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

# BFS
def BFS(x, y):
    queue = deque([(x, y, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    result = 0

    while queue:
        X, Y, count = queue.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= N or Y < 0 or Y >= M: continue
        if Map[X][Y] == 'W': continue
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True
        result = max(result, count)
        
        # 다음 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_, count+1))

    return result

# BFS 돌리기
for x in range(N):
    for y in range(M):
        if Map[x][y] == 'L': result = max(result, BFS(x, y))

# 출력부
print(result)