# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, M, R = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 초기값 선언
visited = [0 for _ in range(N+1)]
count = 1

# DFS
def DFS(node):
    global count

    # 탐색 및 출력부
    visited[node] = count
    count += 1

    # 다음 탐색
    for node_ in sorted(graph[node]):
        # 탐색 불가 조건
        if visited[node_]: continue
        DFS(node_)

# 함수 호출 및 출력부
DFS(R)
for i in range(1, N+1): print(visited[i])