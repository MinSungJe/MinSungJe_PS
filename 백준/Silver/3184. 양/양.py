# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(C)] for _ in range(R)]

# BFS
def BFS(x, y):
    # 초기값 선언
    queue = deque([(x, y)])
    isEscape = False
    sheep, wolf = 0, 0
    if Map[x][y] == 'o': sheep += 1
    if Map[x][y] == 'v': wolf += 1

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C:
                isEscape = True
                continue
            if Map[X_][Y_] == '#': continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            if Map[X_][Y_] == 'o': sheep += 1
            if Map[X_][Y_] == 'v': wolf += 1

            # 다음 탐색
            queue.append((X_, Y_))

    # 탈출 여부 확인
    if isEscape: return 0, 0

    return sheep, wolf


# 모든 영역 탐색
sheep, wolf = 0, 0
for x in range(R):
    for y in range(C):
        if not visited[x][y] and Map[x][y] != '#':
            visited[x][y] = True
            value_sheep, value_wolf = BFS(x, y)

            # 영역 안에서 쫒아냈는지 잡아먹었는지 체크
            if value_sheep > value_wolf: sheep += value_sheep
            else: wolf += value_wolf

# 출력부
print(sheep, wolf)