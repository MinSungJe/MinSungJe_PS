# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 2 위치 찾기
start = list()
for i in range(N):
    for j in range(N):
        if Map[i][j] == 2: start.append((i, j, 0))

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 바이러스가 퍼지는 시간 계산
def BFS(queue):
    result = -1

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= N or Y < 0 or Y >= N: continue
        if Map[X][Y] == 1: continue
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True
        result = max(result, count)

        # 다음 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_, count+1))
        
    return result

# 바이러스가 퍼지는 최소 시간 찾기
result = 2501
for queue in combinations(start, M):
    visited = [[False for _ in range(N)] for _ in range(N)]
    all_spread = True
    value = BFS(deque(queue))
    for i in range(N):
        for j in range(N):
            if Map[i][j] != 1 and not visited[i][j]: all_spread = False
    if all_spread: result = min(result, value) # 바이러스가 모두 퍼졌을 때만 반영

# 출력부
print(result if result != 2501 else -1)