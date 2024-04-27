# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, M, K = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b: graph[a].append((b, c))

# 초기값 선언
INF = 3000001
DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

# DFS
def DFS(node, count):
    if count >= M: return -INF
    if node == N: return 0
    if DP[node][count]: return DP[node][count]

    result = -INF
    for node_, value in graph[node]:
        result = max(result, value+DFS(node_, count+1))

    # 메모이제이션
    DP[node][count] = result
    return result

# 함수 호출 및 출력부
result = DFS(1, 0)
print(result)