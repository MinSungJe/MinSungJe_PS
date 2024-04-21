# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, M = map(int, input().split())
tall = [list() for _ in range(N+1)]
short = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    tall[a].append(b)
    short[b].append(a)

# DFS
def DFS(node, isTall):
    result = 0
    if isTall:
        for node_ in tall[node]:
            if visited[node_][isTall]: continue
            visited[node_][isTall] = True
            result += (1+DFS(node_, isTall))
    else:
        for node_ in short[node]:
            if visited[node_][isTall]: continue
            visited[node_][isTall] = True
            result += (1+DFS(node_, isTall))

    return result

# 탐색 및 결과값 도출
result = 0
for i in range(1, N+1):
    visited = [[False for _ in range(2)] for _ in range(N+1)]
    value = DFS(i, 0)+DFS(i, 1)
    if value == N-1: result += 1

# 출력부
print(result)