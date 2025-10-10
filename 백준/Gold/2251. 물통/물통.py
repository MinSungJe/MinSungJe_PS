# 모듈 불러오기
from collections import deque

# 입력부
A, B, C = map(int, input().split())

# 초기값 선언
visited = [[[False for _ in range(201)] for _ in range(201)] for _ in range(201)]
available_water = set()
available_water.add(C)
queue = deque([(0, 0, C)])

# BFS
while queue:
    a, b, c = queue.popleft()

    # 탐색 불가 조건
    if visited[a][b][c]: continue

    # 탐색
    visited[a][b][c] = True
    if a == 0: available_water.add(c)

    # 다음 탐색
    queue.append((a-min(a, B-b), b+min(a, B-b), c))
    queue.append((a-min(a, C-c), b, c+min(a, C-c)))
    queue.append((a+min(A-a, b), b-min(A-a, b), c))
    queue.append((a, b-min(C-c, b), c+min(C-c, b)))
    queue.append((a+min(c, A-a), b, c-min(c, A-a)))
    queue.append((a, b+min(c, B-b), c-min(c, B-b)))

# 출력부
answer = sorted(list(available_water))
print(*answer)