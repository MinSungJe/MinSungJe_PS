# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, E = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(E):
    A, B, cost = map(int, input().split())
    graph[A].append((cost, B))
    graph[B].append((cost, A))
v1, v2 = map(int, input().split())

# 초기값 선언
INF = 2400000
dist1 = [INF for _ in range(N+1)]
dist1[1] = 0
dist2 = [INF for _ in range(N+1)]
dist2[v1] = 0
dist3 = [INF for _ in range(N+1)]
dist3[v2] = 0

# 다익스트라 알고리즘
def dijkstra(start, result):
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if result[node] < dist: continue

        for value, next in graph[node]:
            dist_ = dist + value
            if result[next] <= dist_: continue
            result[next] = dist_
            heapq.heappush(heap, (dist_, next))

    return result

# 다익스트라 알고리즘 3번 돌리기
dist1 = dijkstra(1, dist1)
dist2 = dijkstra(v1, dist2)
dist3 = dijkstra(v2, dist3)

# 출력부
result = min(dist1[v1]+dist2[v2]+dist3[N], dist1[v2]+dist3[v1]+dist2[N])
if result >= INF: result = -1
print(result)