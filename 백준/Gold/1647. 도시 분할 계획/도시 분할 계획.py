# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 선언
P = [i for i in range(N+1)]
heap = []
result = 0
highValue = 0

# union-find
def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X = find(A)
    Y = find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# 간선 정보 입력
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(heap, (C, A, B))

# 크루스칼 알고리즘
while heap:
    value, node1, node2 = heapq.heappop(heap)

    # 탐색 불가 조건
    if find(node1) == find(node2): continue

    # 탐색
    union(node1, node2)
    result += value
    highValue = max(highValue, value)

# 출력부
print(result-highValue)