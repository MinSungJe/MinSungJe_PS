# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, Q = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(2**N)] for _ in range(2**N)]

# 회전시키는 함수
def rotate(X, Y, size):
    temp = [arr[:] for arr in Map]

    for i in range(size):
        for j in range(size):
            Map[X+i][Y+j] = temp[X+(size-1-j)][Y+i]

# 녹을 얼음 찾아서 녹이는 함수
def melt():
    ice = deque()

    # 녹을 얼음 찾기
    for X in range(2**N):
        for Y in range(2**N):
            if not Map[X][Y]: continue
            count = 4
            for i in range(4):
                X_, Y_ = X+dx[i], Y+dy[i]
                if X_ < 0 or X_ >= 2**N or Y_ < 0 or Y_ >= 2**N or not Map[X_][Y_]: count -= 1
            if count < 3: ice.append((X, Y))

    # 얼음 녹이기
    while ice:
        X, Y = ice.popleft()
        Map[X][Y] -= 1

# 합 구하는 함수
def getSum():
    result = 0
    for i in range(2**N):
        for j in range(2**N):
            result += Map[i][j]
    return result

# BFS 함수
def BFS(x, y):
    # 초기값 선언
    result = 1
    queue = deque([(x, y)])
    visited[x][y] = True

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= 2**N or Y_ < 0 or Y_ >= 2**N: continue
            if not Map[X_][Y_]: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            result += 1

            # 다음 탐색
            queue.append((X_, Y_))

    return result
    
# 파이어스톰
for i in range(Q):
    size = 2 ** L[i]
    for X in range(0, 2**N, size):
        for Y in range(0, 2**N, size):
            rotate(X, Y, size)
    melt()

# 출력부
print(getSum())
result = 0
for i in range(2**N):
    for j in range(2**N):
        if Map[i][j] and not visited[i][j]: result = max(result, BFS(i, j))
print(result)