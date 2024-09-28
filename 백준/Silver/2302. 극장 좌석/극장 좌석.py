# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
M = int(input())
vips = [int(input()) for _ in range(M)]

# DP 배열 선언 및 채우기
DP = [0 for _ in range(41)]
DP[0] = 1
DP[1] = 1
DP[2] = 2
for i in range(3, 41): DP[i] = 2*DP[i-2] + DP[i-3]

# vip로 좌석 쪼개고 결과값 구하기
result = 1
idx = 0
for vip in vips:
    people = vip - idx - 1
    result *= DP[people]
    idx = vip
result *= DP[N-idx]

# 출력부
print(result)