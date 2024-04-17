# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 초기값 선언
result = 10000
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
queue = deque([(0, 0, 0)])
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True

# 0-1 BFS
while queue:
    X, Y, count = queue.popleft()

    # 탐색 완료
    if X == N-1 and Y == M-1:
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]\

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        if Map[X_][Y_]: queue.append((X_, Y_, count+1))
        else: queue.appendleft((X_, Y_, count))

# 출력부
print(result)