# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(n)]

# 시작 지점 찾기
X, Y = -1, -1
for x in range(n):
    for y in range(m):
        if Map[x][y] == 2:
            X, Y = x, y

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(m)] for _ in range(n)]
visited[X][Y] = True
queue = deque([(X, Y, 0)])

# BFS
answer = -1
while queue:
    X, Y, count = queue.popleft()

    # 탐색 종료
    if Map[X][Y] == 3 or Map[X][Y] == 4 or Map[X][Y] == 5:
        answer = count
        break

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 팀색 불가 조건
        if X_ < 0 or X_ >= n or Y_ < 0 or Y_ >= m: continue
        if Map[X_][Y_] == 1: continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        queue.append((X_, Y_, count+1))

# 출력부
if answer == -1: print('NIE')
else:
    print('TAK')
    print(answer)