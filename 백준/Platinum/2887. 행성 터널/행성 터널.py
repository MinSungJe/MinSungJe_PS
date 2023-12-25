# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
stars = []
for idx in range(N):
    X, Y, Z = map(int, input().split())
    stars.append((X, Y, Z, idx))

# 초기값 선언
result = 0
heap = []
P = [i for i in range(N)]

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

# 각 좌표별로 정렬 후 힙에 정보 넣기
stars.sort(key=lambda x:x[0])
for i in range(N-1):
    heapq.heappush(heap, (abs(stars[i][0]-stars[i+1][0]), stars[i][3], stars[i+1][3]))
stars.sort(key=lambda x:x[1])
for i in range(N-1):
    heapq.heappush(heap, (abs(stars[i][1]-stars[i+1][1]), stars[i][3], stars[i+1][3]))
stars.sort(key=lambda x:x[2])
for i in range(N-1):
    heapq.heappush(heap, (abs(stars[i][2]-stars[i+1][2]), stars[i][3], stars[i+1][3]))

# 크루스칼 알고리즘
while heap:
    value, node1, node2 = heapq.heappop(heap)

    # 탐색 불가 조건 : 사이클이 생김
    if find(node1) == find(node2): continue

    # 탐색
    union(node1, node2)
    result += value

# 출력부
print(result)