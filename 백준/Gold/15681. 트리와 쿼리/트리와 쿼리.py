# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, R, Q = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 초기값 선언
DP = [0 for _ in range(N+1)]

# DFS(+DP)
def DFS(node):
    if DP[node]: return 0 # 이미 탐색을 한 상위트리임

    DP[node] = 1
    for node_ in graph[node]:
        DP[node] += DFS(node_)
    
    return DP[node]

# 함수 호출 및 출력부
DFS(R) # DP값 채우기
for _ in range(Q):
    u = int(input())
    print(DP[u])