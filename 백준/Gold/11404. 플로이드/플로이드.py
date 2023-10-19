# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
m = int(input())

# 초기값 선언
INF = 10000001
graph = [[INF if j != i else 0 for j in range(n)] for i in range(n)]

# 그래프 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1] ,c)

# 플로이드 워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력부
for i in range(n):
    for j in range(n):
        if graph[i][j] == INF: graph[i][j] = 0
    print(*graph[i])