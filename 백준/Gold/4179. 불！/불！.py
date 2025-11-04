# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기 위치 확인
startX, startY = 0, 0
fire = deque()
for x in range(R):
    for y in range(C):
        if Map[x][y] == 'J': startX, startY = x, y
        if Map[x][y] == 'F': fire.append((x, y))

# 초기값 선언
INF = 1000001
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[INF for _ in range(C)] for _ in range(R)]


# 불 번지기
for x, y in fire:
    queue = deque([(x, y, 0)])
    
    while queue:
        x, y, count = queue.popleft()
        
        # 탐색 불가 조건
        if x < 0 or x >= R or y < 0 or y >= C: continue
        if Map[x][y] == '#': continue
        if visited[x][y] <= count: continue

        # 탐색
        visited[x][y] = count

        # 다음 탐색
        for i in range(4):
            x_, y_ = x+dx[i], y+dy[i]
            queue.append((x_, y_, count+1))

# 지훈이 이동
answer = 'IMPOSSIBLE'
queue = deque([(startX, startY, 0)])
while queue:
    X, Y, count = queue.popleft()

    # 탈출
    if X < 0 or X >= R or Y < 0 or Y >= C:
        answer = count
        break

    # 탐색 불가 조건
    if Map[X][Y] == '#' or Map[X][Y] == 'F': continue
    if visited[X][Y] <= count: continue

    # 탐색
    visited[X][Y] = count

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        queue.append((X_, Y_, count+1))

# 출력부
print(answer)