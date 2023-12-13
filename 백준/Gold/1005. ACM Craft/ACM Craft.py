# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = [list() for _ in range(N+1)]
    count = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        count[Y] += 1
    W = int(input())

    # 위상 0부터 시작
    queue = deque()
    values = [0 for _ in range(K+1)]
    for i in range(1, N+1):
        if not count[i]: queue.append((i, 0))

    result = [0 for _ in range(N+1)]
    # 위상 정렬 알고리즘
    while queue:
        node, time = queue.popleft()

        time = max(result[node], time)

        if node == W:
            break

        for node_ in graph[node]:
            count[node_] -= 1
            result[node_] = max(result[node_], time+D[node])
            if not count[node_]: queue.append((node_, time+D[node]))
    
    # 출력부
    print(result[W]+D[W])