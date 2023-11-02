# 모듈 불러오기
from collections import deque

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
answer = 0

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 주어진 Map에서 바이러스가 확산되는 함수
def BFS(map):
    # 초기값 선언
    queue = deque()

    # 바이러스 찾기
    for i in range(N):
        for j in range(M):
            if map[i][j] == 2: queue.append((i,j))

    # BFS
    while queue:
        X, Y= queue.popleft()

        # 다음 확산
        for idx in range(4):
            X_ = X + dx[idx]
            Y_ = Y + dy[idx]

            # 확산 불가 조건
            # 1. 탐색하려는 지역은 범위를 벗어남
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
            # 2. 탐색하려는 지역은 빈 곳이 아님
            if map[X_][Y_]: continue
            
            # 확산
            map[X_][Y_] = 2

            queue.append((X_, Y_))
    
    return map

# 안전 구역 개수 구하는 함수
def safe(map):
    result = 0

    for i in range(N):
        for j in range(M):
            if map[i][j] == 0: result += 1
    
    return result

# 벽 세우는 함수
def wall(count):
    global Map, answer
    if count == 3:
        tempMap = [row[:] for row in Map]
        answer = max(answer, safe(BFS(tempMap)))
        return
    
    # 벽 세우기
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                Map[i][j] = 1
                wall(count+1)
                Map[i][j] = 0

# 출력부
wall(0)
print(answer)