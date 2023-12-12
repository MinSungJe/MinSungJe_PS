# 빠른 입력
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 설정
count = [0 for _ in range(N+1)]
graph = [list() for _ in range(N+1)]
result = []
heap = []

# 그래프 입력
for _ in range(M):
    singers = list(map(int, input().split()))
    for i in range(1, singers[0]):
        graph[singers[i]].append(singers[i+1])
        count[singers[i+1]] += 1

# 처음 시작 값 heap에 넣기
for i in range(1, N+1):
    if not count[i]: heapq.heappush(heap, i)

# 위상정렬
while heap:
    node = heapq.heappop(heap)
    # 탐색 및 출력부
    result.append(node)

    # 다음 탐색
    for next_node in graph[node]:
        count[next_node] -= 1
        if not count[next_node]: heapq.heappush(heap, next_node)

# 출력부
if len(result) != N: result = [0]
for i in range(len(result)): print(result[i])