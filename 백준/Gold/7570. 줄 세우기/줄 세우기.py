# 입력부
N = int(input())
children = list(map(int, input().split()))

# DP 배열 선언
DP = [0 for _ in range(1000001)]

# DP 배열 채우기
for i in range(N):
    value = children[i]
    if not DP[value-1]: DP[value] = 1
    else: DP[value] = DP[value-1]+1

# 출력부
print(N-max(DP))