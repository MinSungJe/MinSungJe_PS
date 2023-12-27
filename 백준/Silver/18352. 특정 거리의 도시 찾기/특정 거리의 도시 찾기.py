# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K, X = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((1, B))

# 초기값 선언
INF = 300001
result = [INF for _ in range(N+1)]
result[X] = 0

# 다익스트라 알고리즘
heap = [(0, X)]
while heap:
    dist, node = heapq.heappop(heap)
    
    if dist > result[node]: continue

    # 다음 탐색
    for value, node_ in graph[node]:
        dist_ = dist + value
        if dist_ >= result[node_]: continue

        result[node_] = dist_
        heapq.heappush(heap, (dist_, node_))

# 출력부
answer = []
for i in range(1, N+1):
    if result[i] == K: answer.append(i)
answer.sort()
if answer:
    for ans in answer: print(ans)
else: print(-1)