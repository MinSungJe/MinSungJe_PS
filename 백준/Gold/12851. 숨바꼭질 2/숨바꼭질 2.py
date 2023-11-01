# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())

# 초기값 선언
visited = [[False, 0] for _ in range(200001)]
result = 0
minTime = -1
queue = deque([(N, 0)])

# BFS
while queue:
    current, time = queue.popleft()

    # 탐색 불가 조건
    # 1. 탐색한 지역은 범위를 벗어남
    if current < 0 or current >= 200001: continue
    # 2. 현재 시간은 최소 시간을 벗어남
    if minTime != -1 and time > minTime: continue
    # 3. 탐색한 지역은 이미 전 시점에 방문했음
    if visited[current][0] and visited[current][1] < time: continue

    # 탐색
    if current == K: # 도착
        if minTime == -1: minTime = time # 최소시간 갱신
        result += 1
        continue

    visited[current][0] = True # 방문배열 변경
    visited[current][1] = time

    # 다음 탐색
    queue.append((current-1, time+1))
    queue.append((current+1, time+1))
    queue.append((2*current, time+1))

# 출력부
print(minTime)
print(result)