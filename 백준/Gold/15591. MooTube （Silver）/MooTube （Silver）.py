# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, Q = map(int, input().split())

# 전역변수 선언
INF = 1000000001

# 그래프 그리기
graph = [list() for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

# BFS
def BFS(K, start):
    # 초기값 선언
    visited = [INF for _ in range(N+1)]
    visited[start] = 0
    queue = deque([(start, INF)])

    # 탐색 시작
    while queue:
        node, value = queue.popleft()

        # 다음 탐색
        for node_, value_ in graph[node]:
            # 탐색 불가 조건
            if visited[node_] != INF: continue

            # 탐색
            USADO = min(value, value_)
            visited[node_] = USADO

            # 다음 탐색
            queue.append((node_, USADO))

    # K에 따른 추천 동영상 개수 결정
    result = 0
    for i in range(1, N+1):
        if K <= visited[i]: result += 1
    return result

# 함수 호출 및 출력부
for _ in range(Q):
    k, v = map(int, input().split())
    result = BFS(k, v)
    print(result)