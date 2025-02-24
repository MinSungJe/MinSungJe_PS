# 빠른 입력
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 그래프 그리기
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

# 초기값 선언
INF = 10001
start = 1
visited = [INF for _ in range(N+1)]
visited[start] = 0
heap = [(0, start)]

# 프림 알고리즘
result = [0 for _ in range(N+1)]
while heap:
    dist, node = heapq.heappop(heap)

    # 탐색 불가 조건
    if visited[node] < dist: continue

    # 다음 탐색
    for value, node_ in graph[node]:
        dist_ = dist+value
        
        # 탐색 불가 조건
        if visited[node_] <= dist_: continue

        # 탐색
        visited[node_] = dist_
        result[node_] = node

        # 다음 탐색
        heapq.heappush(heap, (dist_, node_))

# 출력부
print(N-1)
for i in range(1, N+1):
    if result[i] == 0: continue
    print(i, result[i])