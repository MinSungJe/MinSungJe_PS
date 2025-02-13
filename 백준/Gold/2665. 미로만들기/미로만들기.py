# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
Map = [list(map(int, list(input()))) for _ in range(n)]

# 초기값 선언
INF = 2501
queue = deque([(0, 0, 0)])
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[INF for _ in range(n)] for _ in range(n)]
visited[0][0] = 0

# BFS
while queue:
    X, Y, count = queue.popleft()

    # 종료
    if X == n-1 and Y == n-1:
        visited[X][Y] = count
        continue

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 탐색 불가 조건
        if X_ < 0 or X_ >= n or Y_ < 0 or Y_ >= n: continue
        count_ = count+1 if not Map[X_][Y_] else count
        if visited[X_][Y_] <= count_: continue

        # 탐색
        visited[X_][Y_] = count_

        # 다음 탐색
        queue.append((X_, Y_, count_))

# 출력부
result = visited[n-1][n-1]
print(result)