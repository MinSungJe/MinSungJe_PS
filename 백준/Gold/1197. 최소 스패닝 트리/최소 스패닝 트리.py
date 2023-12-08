# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
V, E = map(int, input().split())

# 초기값 선언
result = 0
heap = []
P = [i for i in range(V+1)]

# 간선 정보 힙에 입력
for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(heap, (C, A, B))

# union-find
def find(A):
    if A == P[A]: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X = find(A)
    Y = find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# 크루스칼 알고리즘
while heap:
    dist, node1, node2 = heapq.heappop(heap)

    # 사이클 발생하는 경우 continue
    if find(node1) == find(node2): continue

    # 결과에 추가
    result += dist
    union(node1, node2)

# 출력부
print(result)