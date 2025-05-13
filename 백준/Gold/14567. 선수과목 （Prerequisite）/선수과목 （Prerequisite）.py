# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
graph = [list() for _ in range(N+1)]
phase = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    phase[B] += 1

# 초기값 선언
result = [-1 for _ in range(N+1)]
heap = []
for node in range(1, N+1):
    if phase[node] != 0: continue
    result[node] = 1
    heap.append((1, node))

# 위상 정렬
while heap:
    count, node = heapq.heappop(heap)

    # 결과 반영
    result[node] = max(result[node], count)
    
    # 다음 노드 탐색
    for node_ in graph[node]:
        phase[node_] -= 1
        if phase[node_] != 0: continue
        heapq.heappush(heap, (count+1, node_))

# 출력부
print(*result[1:])