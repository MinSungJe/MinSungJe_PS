# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
startPos = list()
visited = [[False for _ in range(N)] for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 섬 분류 및 출발지점 정하기
def island(x, y, idx):
    # 초기값 선언
    queue = deque([(x, y)])
    visited[x][y] = True
    Map[x][y] = idx

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
            if not Map[X_][Y_]:
                startPos.append((X, Y, idx))
                continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            Map[X_][Y_] = idx

            # 다음 탐색
            queue.append((X_, Y_))

# 함수 호출
mark = 1
for i in range(N):
    for j in range(N):
        if Map[i][j] and not visited[i][j]:
            island(i, j, mark)
            mark += 1

# 시작 지점 간 거리 최솟값 구하기
result = 10001
for A, B in combinations(startPos, 2):
    if A[2] == B[2]: continue
    X1, Y1, X2, Y2 = A[0], A[1], B[0], B[1]
    result = min(result, abs(X1-X2)+abs(Y1-Y2)-1)
    if result == 1: break
print(result)