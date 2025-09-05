# 모듈 불러오기
from collections import deque

# 입력부
N, M, R = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 초기값 선언
answer = [-1 for _ in range(N+1)]
queue = deque([(R, 0)])

# BFS
while queue:
    node, count = queue.popleft()

    # 탐색 불가 조건
    if answer[node] != -1 and answer[node] <= count: continue

    # 탐색
    answer[node] = count

    # 다음 탐색
    for node_ in graph[node]: queue.append((node_, count+1))

# 출력부
for value in answer[1:]: print(value)