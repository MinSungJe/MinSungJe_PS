# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 설정
graph = [list() for _ in range(N+1)]
tall = [0 for _ in range(N+1)]
result = []
heap = []

# 그래프 입력
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    tall[B] += 1

# tall값이 0인 학생부터 투입
for i in range(1, N+1):
    if not tall[i]: heapq.heappush(heap, i)

# heap 탐색
while heap:
    current = heapq.heappop(heap)
    result.append(current)
    for next in graph[current]:
        tall[next] -= 1
        if not tall[next]: heapq.heappush(heap, next)

# 출력부
print(*result)