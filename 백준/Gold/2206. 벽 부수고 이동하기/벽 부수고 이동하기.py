# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
result = -1
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
queue = deque([(0,0,1,False)])
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

# BFS
while queue:
    X, Y, count, isBreak = queue.popleft()

    # 탐색 완료
    if X == N-1 and Y == M-1:
        result = count
        break

    # 탐색 불가 조건
    # 1. 탐색하려는 위치가 범위를 벗어남
    if X < 0 or X >= N or Y < 0 or Y >= M: continue
    # 2. 탐색하려는 위치는 벽임, isBreak가 False인 경우 통과 가능
    if Map[X][Y] == '1':
        if isBreak: continue
        else: isBreak = True
    # 3. 탐색하려는 위치는 이미 탐색한 적이 있음, isBreak 여부에 따라 참고하는 위치가 다름
    if isBreak:
        if visited[X][Y][1]: continue
    else:
        if visited[X][Y][0]: continue

    # 탐색
    if isBreak: visited[X][Y][1] = True
    else: visited[X][Y][0] = True

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        queue.append((X_,Y_,count+1,isBreak))

# 출력부
print(result)