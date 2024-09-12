# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
idx = 1
visited = [[0 for _ in range(M)] for _ in range(N)]
value = [0]

# 그룹핑 함수
def BFS(x, y, idx):
    # 초기값 선언
    queue = deque([(x, y)])
    count = 1
    visited[x][y] = idx

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
            if not Map[X_][Y_]: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = idx
            count += 1

            # 다음 탐색
            queue.append((X_, Y_))
    
    # 결과 반영
    value.append(count)

# 함수 호출
for x in range(N):
    for y in range(M):
        if Map[x][y] and not visited[x][y]:
            BFS(x, y, idx)
            idx += 1

# 결과 도출
result = 0
for x in range(N):
    for y in range(M):
        if Map[x][y]: continue

        # 초기값 선언
        score = 0
        group = list()

        # 4방향 탐색
        for i in range(4):
            x_, y_ = x+dx[i], y+dy[i]

            # 탐색 불가 조건
            if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M: continue

            group.append(visited[x_][y_])
        
        # 모든 중복되지 않는 그룹의 값 더하기
        for i in set(group): score += value[i]
        result = max(result, score+1) # 결과 반영

# 출력부
print(result)