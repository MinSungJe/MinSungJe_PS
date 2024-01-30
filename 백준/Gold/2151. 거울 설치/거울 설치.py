# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 전역변수 선언
# 0: 위 / 1: 아래 / 2: 왼쪽 / 3: 오른쪽
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 초기값 선언
queue = deque()
visited = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]
result = 0

# 문 위치 찾기
door = list()
for i in range(N):
    for j in range(N):
        if Map[i][j] == '#': door.append((i, j))

# queue 채우기
for d in range(4): queue.append((door[0][0], door[0][1], d, 0))

# BFS
while queue:
    X, Y, D, count = queue.popleft()
    
    # 주어진 방향으로 한 칸 탐색
    X_, Y_ = X+dx[D], Y+dy[D]
    
    # 탐색 불가 조건
    if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
    if Map[X_][Y_] == '*': continue
    if visited[X_][Y_][D] != -1 and visited[X_][Y_][D] < count: continue

    # 탐색
    visited[X_][Y_][D] = count
    if X_ == door[1][0] and Y_ == door[1][1]: continue


    # 다음 탐색
    queue.append((X_, Y_, D, count))
    if Map[X_][Y_] == '!':
        if D == 0 or D == 1:
            queue.append((X_, Y_, 2, count+1))
            queue.append((X_, Y_, 3, count+1))
        else:
            queue.append((X_, Y_, 0, count+1))
            queue.append((X_, Y_, 1, count+1))

# 결과값 계산 및 출력부
result = 2501
for d in range(4):
    element = visited[door[1][0]][door[1][1]][d]
    if element == -1: continue
    result = min(result, element)
print(result)