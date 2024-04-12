# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
V, E, P = map(int, input().split())
graph = [list() for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

# 초기값 선언
INF = 50000001

# 다익스트라 함수
def dijkstra(start, end):
    result = [INF for _ in range(V+1)]
    result[start] = 0
    heap = [(start, 0)]

    # 다익스트라
    while heap:
        node, value = heapq.heappop(heap)

        # 탐색 불가 조건
        if value > result[node]: continue

        # 다음 탐색
        for dist, node_ in graph[node]:
            value_ = value+dist
            if value_ >= result[node_]: continue
            result[node_] = value_
            heapq.heappush(heap, (node_, value_))
    
    return result[end]

# 함수 호출 및 출력부
result = dijkstra(1, V) >= dijkstra(1, P) + dijkstra(P, V)
print("SAVE HIM" if result else "GOOD BYE")