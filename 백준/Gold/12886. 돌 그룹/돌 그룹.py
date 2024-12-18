# 모듈 불러오기
from collections import deque

# 입력부
A, B, C = map(int, input().split())

# 초기값 선언
result = 0
queue = deque([(A, B, C)])
visited = [[False for _ in range(1501)] for _ in range(1501)]

# BFS
while queue:
    a, b, c = queue.popleft()
    MAX = max(a,b,c)
    MIN = min(a,b,c)

    # 탐색 불가 조건
    if visited[MAX][MIN]: continue

    # 탐색
    if a == b and b == c and a == c:
        result = 1
        break
    visited[MAX][MIN] = True

    # 다음 탐색
    if a > b: queue.append((a-b, b+b, c))
    if a < b: queue.append((a+a, b-a, c))
    if b > c: queue.append((a, b-c, c+c))
    if b < c: queue.append((a, b+b, c-b))
    if a > c: queue.append((a-c, b, c+c))
    if a < c: queue.append((a+a, b, c-a))

# 출력부
print(result)