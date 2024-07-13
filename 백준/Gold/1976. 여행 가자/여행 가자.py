# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
M = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

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

# 연결 정보 반영
for i in range(N):
    for j in range(N):
        if Map[i][j]: union(i+1, j+1)

# 여행 계획 확인
result = 'YES'
for i in range(M-1):
    city = plan[i]
    city_ = plan[i+1]
    if find(city) != find(city_):
        result = 'NO'
        break

# 출력부
print(result)