# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
cmd = list(map(int, input().split()))[:-1]
N = len(cmd)

# 초기값 선언
INF = 400001

# 이동할 때 드는 힘 기록
power = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    for j in range(5):
        if abs(i-j) == 2: power[i][j] = 4
        else: power[i][j] = 3
        if i == j: power[i][j] = 1
        if i == 0: power[i][j] = 2

# DP Table 선언
DP = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(N)]

# DP Table 채우는 함수(Top-down)
def step(n, l, r):
    if n == N: return 0
    if DP[n][l][r]: return DP[n][l][r]
    
    DP[n][l][r] = min(step(n+1,cmd[n],r)+power[l][cmd[n]], step(n+1,l,cmd[n])+power[r][cmd[n]])
    return DP[n][l][r]

# 함수 호출
print(step(0, 0, 0))