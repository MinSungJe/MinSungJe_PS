# 모듈 불러오기
import sys
from collections import deque
# 빠른 입출력
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기 변수 선언 및 초기값 queue에 대입
queue = deque()
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue.append((0,0,1))

# BFS 시작
while queue:
    # 값 뽑아내기
    temp = queue.popleft()
    X = temp[0]
    Y = temp[1]
    move = temp[2]

    # 도착
    if X == N-1 and Y == M-1:
        print(move)
        break

    # 탐색이 불가능한 경우
    # 1. 좌표가 맵 바깥으로 벗어남
    if X < 0 or X >= N or Y < 0 or Y >= M: continue
    # 2. 해당 좌표는 이동할 수 없는 칸임
    if Map[X][Y] == '0': continue
    # 3. 해당 좌표는 이미 방문한 적 있는 칸임
    if visited[X][Y]: continue

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        queue.append((X_,Y_,move+1))