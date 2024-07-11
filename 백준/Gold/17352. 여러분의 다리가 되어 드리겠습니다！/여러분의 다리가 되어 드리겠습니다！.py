# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# union-find
P = [i for i in range(N+1)]
def find(A):
    if A == P[A]: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X, Y = find(A), find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# 그래프 잇기
for _ in range(N-2):
    A, B = map(int, input().split())
    union(A, B)

# 두 부모노드 구하기
result = set()
for i in range(1, N+1): result.add(find(i))

# 출력부
print(*result)