# 빠른 입력 및 모듈 불러오기
from itertools import permutations
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(M)]

# 전역변수 선언
INF = 12501
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 위치 탐색
start = [0, 0]
end = [0, 0]
stuff = list()
for x in range(M):
    for y in range(N):
        if Map[x][y] == 'S': start[0], start[1] = x, y
        if Map[x][y] == 'E': end[0], end[1] = x, y
        if Map[x][y] == 'X': stuff.append((x, y))

# 두 점 사이의 최소거리를 구하는 함수
def getDist(x1, y1, x2, y2):
    # 초기값 선언
    result = 0
    queue = deque([(x1, y1, 0)])
    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[x1][y1] = True

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 도착
        if X == x2 and Y == y2:
            result = count
            break

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= M or Y_ < 0 or Y_ >= N: continue
            if Map[X_][Y_] == '#': continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True

            # 다음 탐색
            queue.append((X_, Y_, count+1))
    
    return result

# 최소값 구하기
result = INF
for sequence in permutations(list(range(len(stuff)))):
    value = 0
    pos = [start[0], start[1]]
    for i in range(len(stuff)):
        value += getDist(pos[0], pos[1], stuff[sequence[i]][0], stuff[sequence[i]][1])
        pos = [stuff[sequence[i]][0], stuff[sequence[i]][1]]
    value += getDist(pos[0], pos[1], end[0], end[1])

    result = min(result, value)

# 출력부
print(result)