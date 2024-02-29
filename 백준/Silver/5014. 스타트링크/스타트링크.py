# 모듈 불러오기
from collections import deque

# 입력부
F, S, G, U, D = map(int, input().split())

# 초기값 선언
result = -1
queue = deque([(S, 0)])
visited = [False for _ in range(F+1)]

# BFS
while queue:
    floor, count = queue.popleft()

    # 탐색 불가 조건
    if floor <= 0 or floor > F: continue
    if visited[floor]: continue

    # 탐색
    if floor == G:
        result = count
        break
    visited[floor] = True

    # 다음 탐색
    queue.append((floor+U, count+1))
    queue.append((floor-D, count+1))

# 출력부
print(result if result != -1 else "use the stairs")