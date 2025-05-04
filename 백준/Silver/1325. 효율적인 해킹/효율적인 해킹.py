# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# BFS
def BFS(start):
    # 초기값 선언
    queue = deque([start])
    visited = [0 for _ in range(N+1)]
    visited[start] = True

    # 탐색
    while queue:
        node = queue.popleft()

        # 다음 탐색
        for node_ in graph[node]:
            # 탐색 불가 조건
            if visited[node_] == 1: continue

            # 탐색
            visited[node_] = 1
            queue.append(node_)

    return sum(visited)

# 오름차순으로 컴퓨터 확인
result_value = [0 for _ in range(N+1)]
for i in range(1, N+1): result_value[i] = BFS(i)

# 결과 도출 및 출력부
result = []
max_value = max(result_value)
for i in range(1, N+1):
    value = result_value[i]
    if value == max_value: result.append(i)
print(*result)