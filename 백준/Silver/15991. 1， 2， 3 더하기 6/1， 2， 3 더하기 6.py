# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# DP 배열 선언
INF = 1000000009
DP = [0 for _ in range(100001)]
DP[0] = 1
DP[1] = 1
DP[2] = 2
DP[3] = 2
for i in range(4, 100001):
    if i < 6: DP[i] = (DP[i-2]+DP[i-4]) % INF
    else: DP[i] = (DP[i-2]+DP[i-4]+DP[i-6]) % INF

# 입력부
T = int(input())
for _ in range(T):
    n = int(input())
    # 출력부
    print(DP[n])