# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
INF = 1000001
result = INF
DP = [[[INF for _ in range(3)] for _ in range(3)] for _ in range(N)]
DP[0][0][0] = Map[0][0]
DP[0][1][1] = Map[0][1]
DP[0][2][2] = Map[0][2]

# DP 배열 채우기
for node in range(1, N):
    for house in range(3):
        for start in range(3):
            if house == 0:
                DP[node][house][start] = Map[node][house] + min(DP[node-1][1][start], DP[node-1][2][start])
            if house == 1:
                DP[node][house][start] = Map[node][house] + min(DP[node-1][0][start], DP[node-1][2][start])
            if house == 2:
                DP[node][house][start] = Map[node][house] + min(DP[node-1][0][start], DP[node-1][1][start])

            if node == N-1 and start == house:
                DP[node][house][start] = INF

# 출력부
for i in range(3):
    result = min(result, min(DP[N-1][i]))
print(result)