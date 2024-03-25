# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)] + [[0, 0]]

# 왼쪽 전봇대 기준으로 정렬
lines.sort()

# DP 배열 선언
DP = [0 for _ in range(N+1)]
DP[1] = 1

# LIS
for i in range(2, N+1):
    for j in range(0, i):
        if lines[i][1] > lines[j][1]: DP[i] = max(DP[i], DP[j]+1)

# 출력부
print(N-max(DP))