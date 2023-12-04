# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 선언
P = [i for i in range(N)]
result = 0

# find
def find(A):
    if A == P[A]: return A
    P[A] = find(P[A])
    return P[A]

# union
def union(A, B):
    X = find(A)
    Y = find(B)
    
    if X == Y: return
    if X > Y: P[X] = Y
    else: P[Y] = X
    return

# 케이스 확인
count = 0
for _ in range(M):
    a, b = map(int, input().split())
    count += 1
    if find(a) == find(b): # 같은 루트노드면 사이클 형성
        result = count
        break
    union(a, b) # 다른 루트노드이므로 엮어줌

# 출력부
print(result)