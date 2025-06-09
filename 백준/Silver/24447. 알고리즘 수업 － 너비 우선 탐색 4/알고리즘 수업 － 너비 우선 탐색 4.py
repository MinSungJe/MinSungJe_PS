# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, R = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 초기값 선언
t = [0 for _ in range(N+1)]
d = [-1 for _ in range(N+1)]
heap = [(0, R)]

# BFS
t_value = 1
while heap:
    count, node = heapq.heappop(heap)

    # 탐색 불가 조건
    if d[node] != -1: continue

    # 탐색
    d[node] = count
    t[node] = t_value
    t_value += 1

    # 다음 탐색
    for node_ in graph[node]: heapq.heappush(heap, (count+1, node_))

# 결과 도출 및 출력부
answer = 0
for i in range(1, N+1): answer += d[i] * t[i]
print(answer)