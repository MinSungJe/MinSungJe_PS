# 모듈 불러오기
from collections import deque

# 입력부
n = int(input())
A = list(map(int, input().split()))
s = int(input())

# 초기값 선언
queue = deque([s-1])
visited = [0 for _ in range(n)]

# BFS
while queue:
    node = queue.popleft()

    # 탐색 불가 조건
    if node < 0 or node >= n: continue
    if visited[node]: continue

    # 탐색
    visited[node] = 1

    # 다음 탐색
    value = A[node]
    for node_ in (node+value, node-value): queue.append(node_)

# 출력부
print(sum(visited))