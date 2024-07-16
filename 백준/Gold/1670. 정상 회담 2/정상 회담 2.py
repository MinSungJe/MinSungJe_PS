# 입력부
N = int(input())

# DP 배열 선언
DP = [0 for _ in range(10001)]
DP[0] = 1
DP[2] = 1

# DP 배열 채우기
for i in range(4, N+1, 2):
    for j in range(0, i//2, 2):
        idx = (i-2)-j # 반대쪽 idx 계산
        if i % 4 != 0 and j == idx: DP[i] += ((DP[j]*DP[idx])) % 987654321 # 한번만 나오는 경우
        else: DP[i] += ((DP[j]*DP[idx]) * 2) % 987654321
    DP[i] %= 987654321

# 출력부
print(DP[N])