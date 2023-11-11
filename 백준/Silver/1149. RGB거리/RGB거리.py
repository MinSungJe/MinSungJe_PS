# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# DP Table 선언 및 채우기
DP = [[0,0,0] for _ in range(N)]
DP[0] = Map[0]
for i in range(1,N):
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + Map[i][0]
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + Map[i][1]
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + Map[i][2]

# 출력부
print(min(DP[N-1]))