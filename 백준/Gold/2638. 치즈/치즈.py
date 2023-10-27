# 모듈 불러오기
from collections import deque

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
result = 0

# Map이 전부 0이 될때까지 반복
while Map != visited:
    # BFS
    queue = deque([(0,0)])
    while queue:
        X, Y = queue.popleft()

        # 탐색 불가 조건
        # 1. 탐색하려는 구역이 Map을 벗어남
        if X < 0 or X >= N or Y < 0 or Y >= M: continue
        # 2. 탐색하려는 구간이 치즈인경우, visited 값을 추가하고 멈춤
        if Map[X][Y] == 1:
            visited[X][Y] += 1
            continue
        # 3. 탐색하려는 곳은 이미 탐색한 적 있는 구역임
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] += 1

        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queue.append((X_, Y_))

    # 시간 추가 및 Map 수정
    result += 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2: Map[i][j] = 0 # 녹아 없어진 치즈
    
    # visited 배열 초기화
    visited = [[0 for _ in range(M)] for _ in range(N)]

# 출력부
print(result)