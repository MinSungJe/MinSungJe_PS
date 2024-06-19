# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
canSee = list(map(int, input().split()))
canSee[N-1] = 0 # 시야를 안보이게 변경
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if canSee[a] or canSee[b]: continue # 보이는 경우 아예 고려 X
    graph[a].append((t, b))
    graph[b].append((t, a))

# 초기값 선언
INF = 10000000001
result = [INF for _ in range(N)]
result[0] = 0
heap = [(0, 0)]

# 다익스트라 알고리즘
while heap:
    value, node = heapq.heappop(heap)

    # 탐색 불가 조건
    if value > result[node]: continue

    # 다음 탐색
    for dist, node_ in graph[node]:
        value_ = value + dist
        # 탐색 불가 조건
        if value_ >= result[node_]: continue

        # 탐색 및 다음 탐색 넣기
        result[node_] = value_
        heapq.heappush(heap, (value_, node_))

# 출력부
print(result[N-1] if result[N-1] < INF else -1)