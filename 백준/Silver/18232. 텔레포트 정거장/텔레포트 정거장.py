# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
S, E = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 이동 정보 담기
for node in range(1, N+1):
    for node_ in (node-1, node+1):
        if node_ < 1: continue
        if node_ > N: continue
        graph[node].append(node_)

# 초기값 선언
visited = [False for _ in range(N+1)]
queue = deque([(S, 0)])

# BFS
count = -1
while queue:
    node, count = queue.popleft()

    # 탐색 불가 조건
    if visited[node]: continue

    # 탐색
    if node == E:
        result = count
        break

    visited[node] = True

    # 다음 탐색
    for node_ in graph[node]: queue.append((node_, count+1))

# 출력부
print(result)