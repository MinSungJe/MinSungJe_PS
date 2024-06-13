# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, M = map(int, input().split())
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
def DFS(node, count):
    # 탐색 불가 조건
    if visited[node]: return 0
    if count >= 5: return 1

    # 탐색
    visited[node] = True

    # 다음 탐색
    result = 1
    for node_ in graph[node]:
        result = max(result, 1+DFS(node_, count+1))
    
    # 백트래킹
    visited[node] = False
    return result

# 함수 호출 및 출력부
result = 0
for i in range(N):
    visited = [False for _ in range(N+1)]
    value = DFS(i, 1)
    if value >= 5:
        result = 1
        break
print(result)