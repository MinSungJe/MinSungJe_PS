# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# union-find
def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X, Y = find(A), find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, M = map(int, input().split())

    # 초기값 선언
    P = [i for i in range(N+1)]
    result = 0

    # 크루스칼 알고리즘
    for _ in range(M):
        A, B = map(int, input().split())
        if find(A) == find(B): continue
        result += 1
        union(A, B)
    
    # 출력부
    print(result)