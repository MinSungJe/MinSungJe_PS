# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()
# 초기값 선언
DP = [0 for _ in range(1000001)]
DP[0] = 1
DP[1] = 1
DP[2] = 2

# DP 배열 채우기
for i in range(3, 1000001):
    DP[i] = (DP[i-3] + DP[i-2] + DP[i-1]) % 1000000009

# 입력부 및 출력부
T = int(input())
for _ in range(T):
    n = int(input())
    print(DP[n])