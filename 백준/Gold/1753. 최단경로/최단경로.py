# 빠른 입력 및 모듈 불러오기
import heapq, sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
V, E = map(int, input().split())
start = int(input())

# 초기값 설정
heap = [(0, start)]
INF = 200001
result = [INF for _ in range(V+1)]
result[start] = 0
graph = [list() for _ in range(V+1)]

# 그래프 입력
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

# 다익스트라 시작
while heap:
    dist, current = heapq.heappop(heap)

    # 탐색 불가 조건 : 현재 dist는 기록된 dist보다 거리가 김
    if dist > result[current]: continue

    # 다음 탐색
    for next, value in graph[current]:
        dist_ = dist + value

        # 다음 탐색 불가 조건 : 다음 dist는 기록된 dist보다 거리가 짧지 않음
        if dist_ >= result[next]: continue
        
        # 탐색
        result[next] = dist_

        # heap에 넣기
        heapq.heappush(heap, (dist_, next))

# 출력부
for ans in result[1:]:
    print(ans if ans != INF else "INF")