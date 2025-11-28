# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
m = int(input())
graph = [list() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 초기값 선언
answer = 0
queue = deque([(1, 0)])
visited = [False for _ in range(n+1)]

# BFS
while queue:
    node, count = queue.popleft()

    # 탐색 불가 조건
    if count > 2: continue
    if visited[node]: continue

    # 탐색
    if node != 1: answer += 1
    visited[node] = True

    # 다음 탐색
    for node_ in graph[node]: queue.append((node_, count+1))

# 출력부
print(answer)