# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m = map(int, input().split())
INF = 933750001
result = [[0 if i == j else INF for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    result[u][v] = 0
    if b == 0: result[v][u] = 1
    else: result[v][u] = 0

# 플로이드-워셜
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            distance = result[i][k] + result[k][j]
            result[i][j] = min(result[i][j], distance)

# 출력부
k = int(input())
for _ in range(k):
    s, e = map(int, input().split())
    print(result[s][e])