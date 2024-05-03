# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
pos = [[0,0]]+[list(map(int, input().split())) for _ in range(N)]
link = [list(map(int, input().split())) for _ in range(M)]

# 거리 구하는 함수
def dist(A, B): return ((pos[A][0]-pos[B][0])**2 + (pos[A][1]-pos[B][1])**2)**(1/2)

# 그래프 그리기
graph = [list() for _ in range(N+1)]
for A in range(1, N+1):
    for B in range(A+1, N+1):
        distance = dist(A, B)
        graph[A].append((distance, B))
        graph[B].append((distance, A))
for A, B in link:
    graph[A].append((0, B))
    graph[B].append((0, A))

# 프림 알고리즘
def Prim(node):
    # 초기값 선언
    result = 0
    heap = list()
    visited = [False for _ in range(N+1)]
    visited[node] = True

    # 초기 간선 그래프에 넣기
    for info in graph[node]: heapq.heappush(heap, info)

    # 탐색
    while heap:
        dist_, node_ = heapq.heappop(heap)

        # 이미 탐색한 노드는 건너뜀
        if visited[node_]: continue

        # 탐색
        result += dist_
        visited[node_] = True
        for info in graph[node_]: heapq.heappush(heap, info)

    return result

print(f'{Prim(1):.2f}')