# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [[list() for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x, y, a, b = map(int, input().split())
    Map[x][y].append((a, b))

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
light = [[False for _ in range(N+1)] for _ in range(N+1)]
light[1][1] = True
visited = [[False for _ in range(N+1)] for _ in range(N+1)]

# 불 켜기
queue = deque([(1, 1)])
while queue:
    X, Y = queue.popleft()
    
    # 탐색 불가 조건
    if X <= 0 or X > N or Y <= 0 or Y > N: continue
    if not light[X][Y]: continue
    if visited[X][Y]: continue

    # 탐색
    visited[X][Y] = True
    for x, y in Map[X][Y]:
        light[x][y] = True
        isAdd = False
        for i in range(4):
            x_, y_ = x+dx[i], y+dy[i]
            if x_ <= 0 or x_ > N or y_ <= 0 or y_ > N: continue
            if visited[x_][y_]: isAdd = True
        if isAdd: queue.append((x, y))

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        queue.append((X_, Y_))

# 결론 도출 및 출력부
answer = 0
for x in range(N+1):
    for y in range(N+1):
        if light[x][y]: answer += 1
print(answer)