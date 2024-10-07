# 입력부
N = int(input())

# DP 배열 채우기
DP = [False for _ in range(1001)]
DP[1] = True
DP[3] = True
DP[4] = True
for i in range(5, 1001):
    if not DP[i-1]: DP[i] = True
    if not DP[i-3]: DP[i] = True
    if not DP[i-4]: DP[i] = True

# 출력부
print('SK' if DP[N] else 'CY')