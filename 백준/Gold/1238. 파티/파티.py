# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, X = map(int, input().split())

# 초기값 선언
INF = 100001
graph = [list() for _ in range(N+1)]
rGraph = [list() for _ in range(N+1)]

# 그래프 입력
for _ in range(M):
    S, E, C = map(int, input().split())
    graph[S].append((C, E))
    rGraph[E].append((C, S))


# 다익스트라 알고리즘
def dijkstra(Graph):
    result = [0] + [INF for _ in range(N)]
    heap = [(0,X)]
    result[X] = 0

    # 알고리즘 시작
    while heap:
        dist, node = heapq.heappop(heap)

        # 현재 거리는 기록된 거리보다 더 김
        if dist > result[node]: continue

        # 다음 탐색
        for value, next in Graph[node]:
            dist_ = dist + value
            # 계산된 거리는 기록된 거리보다 짧지 않음
            if dist_ >= result[next]: continue

            # 거리 최신화
            result[next] = dist_
            # heap에 다음 값 집어 넣음
            heapq.heappush(heap, (dist_, next))
    
    return result

# 일반 그래프와 뒤집힌 그래프 결과 배열 가져오기
path = dijkstra(graph)
rPath = dijkstra(rGraph)

# 최댓값 계산
answer = 0
for i in range(1,N+1):
    answer = max(answer, path[i]+rPath[i])

# 출력부
print(answer)