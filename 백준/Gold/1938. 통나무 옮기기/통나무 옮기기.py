# 빠른 입력 및 모둘 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 시작점과 도착점 확인
startPos, endPos = [0, 0, 0, 0], [0, 0, 0]
start = list()
end = list()
for i in range(N):
    for j in range(N):
        if Map[i][j] == 'B': start.append((i, j))
        if Map[i][j] == 'E': end.append((i, j))
startPos[0], startPos[1], endPos[0], endPos[1] = start[1][0], start[1][1], end[1][0], end[1][1]
if start[0][0] != start[1][0]: startPos[2] = 1
if end[0][0] != end[1][0]: endPos[2] = 1

# 초기값 선언
result = 0
queue = deque([startPos])
visited = [[[False, False] for _ in range(N)] for _ in range(N)]
dx = (-1, 1, 0, 0, -1, -1, 1, 1)
dy = (0, 0, -1, 1, -1, 1, -1, 1)

# BFS
while queue:
    X, Y, rotate, count = queue.popleft()

    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= N: continue
    if Map[X][Y] == '1': continue
    canFind = True
    if rotate:
        for X_ in (X-1, X+1):
            if X_ < 0 or X_ >= N or Map[X_][Y] == '1':
                canFind = False
                break
    else:
        for Y_ in (Y-1, Y+1):
            if Y_ < 0 or Y_ >= N or Map[X][Y_] == '1':
                canFind = False
                break
    if not canFind: continue
    if visited[X][Y][rotate]: continue

    # 탐색
    visited[X][Y][rotate] = True
    if X == endPos[0] and Y == endPos[1] and rotate == endPos[2]: # 탐색 완료
        result = count
        break
    canRotate = True
    for i in range(8):
        X_, Y_ = X+dx[i], Y+dy[i]
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N or Map[X_][Y_] == '1':
            canRotate = False
            break
    
    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        queue.append((X_, Y_, rotate, count+1))
    if canRotate: queue.append((X, Y, not rotate, count+1))

# 출력부
print(result)