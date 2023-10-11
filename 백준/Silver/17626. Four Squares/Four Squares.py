# 모듈 불러오기
from collections import deque

# 입력부
n = int(input())

# 초기값 선언
visited = [False for _ in range(n+1)]
queue = deque()
queue.append((0,0))

# BFS
while queue:
    value, count = queue.popleft()

    # 탐색 완료
    if value == n:
        print(count)
        break

    for i in range(1, 224): # N 조건 상 최댓값은 223
        next = value + (i*i)

        # 탐색 불가 조건 : 다음 위치가 목표를 넘어섬
        if next > n: break
        # 탐색 불가 조건 : 이미 적은 횟수로 도달한 적 있는 숫자임
        if visited[next]: continue

        # 방문 처리
        visited[next] = True

        # 다음 탐색
        queue.append((next, count+1))