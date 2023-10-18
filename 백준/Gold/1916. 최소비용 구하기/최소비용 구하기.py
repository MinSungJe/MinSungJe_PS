# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
M = int(input())

# 초기값 선언
INF = 100000001
result = [0] + [INF for _ in range(N)]
graph = [list() for _ in range(N+1)]

# 그래프 입력
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 비용이 heap의 기준이므로 비용 먼저 기록

# 출발지점, 목표지점 기록
start, end = map(int, input().split())
result[start] = 0
queue = [(0,start)]

# 다익스트라
while queue:
    W, node = heapq.heappop(queue)

    # 탐색 불가 조건 : 값이 최단거리가 아님
    if W > result[node]: continue

    # 다음 탐색
    for value, node_ in graph[node]:
        W_ = W + value
        # 탐색 불가 조건 : 값이 최단거리가 아님
        if W_ >= result[node_]: continue

        # 탐색
        result[node_] = W_

        # queue에 값 입력
        heapq.heappush(queue, (W_, node_))

# 출력부
print(result[end])