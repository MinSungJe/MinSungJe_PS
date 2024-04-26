# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
people = [0] + list(map(int, input().split()))
graph = [list() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 초기값 선언
DP = [[0, 0] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

# DFS(+DP)
def DFS(node):
    visited[node] = True
    DP[node][1] = people[node]
    for node_ in graph[node]:
        if visited[node_]: continue
        DFS(node_)
        DP[node][0] += max(DP[node_])
        DP[node][1] += DP[node_][0]

# 함수 호출 및 출력부
DFS(1)
print(max(DP[1]))