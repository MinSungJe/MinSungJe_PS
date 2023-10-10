# 입력 및 선언
N = int(input())
edge = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
M = int(input())
for _ in range(M):
    A,B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

# dfs 선언
def dfs(N):
    # 이미 탐색됨
    if visited[N]: return

    # 탐색
    visited[N] = 1

    for next in edge[N]:
        dfs(next)

dfs(1)
print(sum(visited)-1)