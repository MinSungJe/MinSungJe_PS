# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K = map(int, input().split())
candy = [0] + list(map(int, input().split()))
bucket = [[0,0] for _ in range(N+1)]

# union-find
P = [i for i in range(N+1)]

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

# 관계 입력
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

# 무리의 수와 사탕 개수 계산
for i in range(1, N+1):
    bucket[find(i)][0] += 1
    bucket[find(i)][1] += candy[i]

# Knapsack (1차원 배열)
DP = [0 for _ in range(K+1)]
for i in range(1, N+1):
    cry = bucket[i][0]
    value = bucket[i][1]
    if not cry: continue
    for j in range(K, cry-1, -1): DP[j] = max(DP[j-cry]+value, DP[j])

# 출력부
print(DP[K-1])