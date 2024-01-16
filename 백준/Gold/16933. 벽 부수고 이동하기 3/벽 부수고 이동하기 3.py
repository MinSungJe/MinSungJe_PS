# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 초기값 설정
result = -1
visited = [[K+1 for _ in range(M)] for _ in range(N)]
queue = deque([(0, 0, 0, 1)])

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS
while queue:
    X, Y, B, count = queue.popleft()
    isDay = count % 2 # 낮인지 밤인지 확인

    if X == N-1 and Y == M-1: # 도착
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        if visited[X_][Y_] <= B: continue

        # 탐색
        if not Map[X_][Y_]: # 벽이 아닌 경우
            visited[X_][Y_] = B
            queue.append((X_, Y_, B, count+1))

        else: # 벽인 경우
            if B+1 > K: continue
            if isDay: # 현재 낮임
                visited[X_][Y_] = B+1
                queue.append((X_, Y_, B+1, count+1))
            else: # 현재 밤임
                queue.append((X, Y, B, count+1)) # 카운트만 한번 올린다

# 출력부
print(result)