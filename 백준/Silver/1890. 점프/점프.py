# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
DP = [[0 for _ in range(N)] for _ in range(N)]
DP[0][0] = 1

# Bottom-Up
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            if i+Map[i][j] < N: DP[i+Map[i][j]][j] += DP[i][j]
            if j+Map[i][j] < N: DP[i][j+Map[i][j]] += DP[i][j]

# 출력부
print(DP[N-1][N-1])