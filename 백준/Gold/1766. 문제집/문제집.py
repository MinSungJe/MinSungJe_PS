# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 선언
graph = [list() for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
heap = []
result = []

# 문제 정보 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

# heap에 진입차수가 0인 노드 넣기
for i in range(1,N+1):
    if not degree[i]: heapq.heappush(heap, i)

# heap을 돌며 문제 순서 탐색
while heap:
    node = heapq.heappop(heap)
    result.append(node)
    
    for next in graph[node]:
        degree[next] -= 1
        if not degree[next]: heapq.heappush(heap, next)

# 출력부
print(*result)