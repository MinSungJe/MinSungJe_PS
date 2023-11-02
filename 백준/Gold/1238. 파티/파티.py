# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, X = map(int, input().split())

# 초기값 선언
INF = 100001
graph = [list() for _ in range(N+1)]

# 그래프 입력
for _ in range(M):
    S, E, C = map(int, input().split())
    graph[S].append((C, E))

# 다익스트라 알고리즘
def dijkstra(start, end):
    result = [0] + [INF for _ in range(N)]
    heap = [(0,start)]
    result[start] = 0

    # 알고리즘 시작
    while heap:
        dist, node = heapq.heappop(heap)

        # 현재 거리는 기록된 거리보다 더 김
        if dist > result[node]: continue

        # 다음 탐색
        for value, next in graph[node]:
            dist_ = dist + value
            # 계산된 거리는 기록된 거리보다 짧지 않음
            if dist_ >= result[next]: continue

            # 거리 최신화
            result[next] = dist_
            # heap에 다음 값 집어 넣음
            heapq.heappush(heap, (dist_, next))
    
    return result[end]


# 모든 노드 다익스트라 검사
answer = 0
for idx in range(1,N+1):
    answer = max(answer, dijkstra(idx, X) + dijkstra(X, idx))

# 출력부
print(answer)