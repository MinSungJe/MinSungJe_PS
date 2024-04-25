# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 바이러스 찾기
virus = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 2: virus.append((i, j, 0))

# 주어진 바이러스 정보와 지도를 이용한 BFS 탐색
def BFS(V, board):
    # 초기값 설정
    M = [arr[:] for arr in board]
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque(V)
    result = 0

    # BFS
    while queue:
        X, Y, time = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_, time_ = X+dx[i], Y+dy[i], time + 1

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
            if M[X_][Y_] == 1: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            if not M[X_][Y_]: result = max(result, time_)
            M[X_][Y_] = 2

            # 다음 탐색
            queue.append((X_, Y_, time_))
    
    # 빈 공간이 있는지 확인
    for i in range(N):
        for j in range(N):
            if not M[i][j]: return 2501

    return result

# 함수 호출 및 출력부
result = 2501
for v in combinations(virus, M):
    result = min(result, BFS(v, Map))
print(result if result < 2501 else -1)