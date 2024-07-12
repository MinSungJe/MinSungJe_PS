# 모듈 불러오기 및 빠른 입력
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# BFS 함수 선언
def BFS(start_node):
    # 초기값 선언\
    queue = deque([(start_node, 0)])
    result = True

    # BFS
    while queue:
        node, Type = queue.popleft()

        # 탐색 불가 조건
        if group[node] != -1:
            if group[node] != Type: # 이분그래프가 아님
                return False
            continue

        # 탐색
        group[node] = Type

        # 다음 탐색
        Type_ = 1 - Type
        for node_ in graph[node]:
            queue.append((node_, Type_))

    return result

# TC
K = int(input())
for test_case in range(1, K+1):
    # 입력부
    V, E = map(int, input().split())
    graph = [list() for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 초기값 선언
    group = [-1 for _ in range(V+1)]

    # 모든 정점 탐색
    result = True
    for node in range(1, V+1):
        if group[node] != -1: continue
        if not BFS(node):
            result = False
            break

    # 출력부
    print('YES' if result else 'NO')