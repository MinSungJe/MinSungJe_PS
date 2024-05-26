# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
school = [0] + list(input().split())

# 간선 정보 넣기
heap = []
for _ in range(M):
    A, B, value = map(int, input().split())
    if school[A] == school[B]: continue # 같은 학교 간선 거르기

    heapq.heappush(heap, (value, A, B))

# union-find
P = [i for i in range(N+1)]

def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X, Y = find(A), find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# 크루스칼 알고리즘
result = 0
count = 0
while heap:
    value, A, B = heapq.heappop(heap)
    
    # 사이클 발생
    if find(A) == find(B): continue

    # 간선 추가
    result += value
    count += 1
    union(A, B)

# 출력부
print(result if count == N-1 else -1)