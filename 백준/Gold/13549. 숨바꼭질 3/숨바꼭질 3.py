# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())

# 초기값 선언
queue = deque()
queue.append((N,0))
visited = [False for _ in range(100001)]

while queue:
    current, time = queue.popleft()
    # 도착
    if current == K:
        print(time)
        break

    # 탐색 불가 조건
    # 1. 현재 위치가 범위를 벗어남
    if current < 0 or current > 100000: continue
    # 2. 현재 위치는 이미 방문한 적 있음
    if visited[current]: continue

    # 탐색
    visited[current] = True

    # 다음 탐색
    if current: queue.appendleft((2*current, time))
    queue.append((current-1, time+1))
    queue.append((current+1, time+1))