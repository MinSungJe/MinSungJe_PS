# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
V, E = map(int, input().split())
INF = 4000001
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A][B] = C

# 플로이드-워셜 알고리즘
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1): graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 결과값 계산 및 출력부
result = INF
for start in range(1, V+1):
    result = min(result, graph[start][start])
print(result if result < INF else -1)