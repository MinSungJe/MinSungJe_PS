# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
INF = 150000
graph = [[0 if i == j else INF for i in range(n)] for j in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

# 플로이드-워셜 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 얻을 수 있는 아이템 최대값 계산
result = 0
for row in graph:
    getItem = 0
    for i in range(n):
        if row[i] > m: continue # 거리가 수색범위보다 큼
        getItem += items[i]
    result = max(result, getItem)

# 출력부
print(result)