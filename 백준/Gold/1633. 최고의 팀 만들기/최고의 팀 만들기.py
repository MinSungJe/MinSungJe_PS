# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
team = list()
while True:
    try:
        # 입력부
        W, B = map(int, input().split())
        team.append((W, B))
    except: break

# 초기값 선언
N = len(team)
DP = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(N)]

# Bottom-Up DP
for i in range(N):
    for j in range(16):
        for k in range(16):
            DP[i][j][k] = DP[i-1][j][k] # 추가하지 않은 경우 반영
            if j > 0: DP[i][j][k] = max(DP[i][j][k], DP[i-1][j-1][k] + team[i][0]) # 백으로 추가
            if k > 0: DP[i][j][k] = max(DP[i][j][k], DP[i-1][j][k-1] + team[i][1]) # 흑으로 추가

# 출력부
result = DP[N-1][15][15]
print(result)