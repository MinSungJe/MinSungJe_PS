# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
school = [0] + list(input().split())

# 초기값 선언
INF = 10000001

# 그래프 그리기
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B, value = map(int, input().split())
    if school[A] == school[B]: continue # 같은 종류의 대학교 간선 거르기

    graph[A].append((value, B))
    graph[B].append((value, A))

# 프림 알고리즘
def Prim(start):
    visited = [False for _ in range(N+1)]
    visited[start] = True
    result = 0
    count = 1
    heap = list()

    # 처음 노드 넣기
    for info in graph[start]: heapq.heappush(heap, info)

    while heap:
        value, node = heapq.heappop(heap)

        # 탐색 불가 조건
        if visited[node]: continue
        
        # 탐색
        visited[node] = True
        result += value
        count += 1

        # 다음 탐색
        for info in graph[node]: heapq.heappush(heap, info)

    return result if count == N else INF

# 함수 호출 및 출력부
result = INF
for start in range(1, N+1): result = min(result, Prim(start))
print(result if result < INF else -1)