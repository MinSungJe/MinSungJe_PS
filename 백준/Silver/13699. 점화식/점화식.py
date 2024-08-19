# 입력부
n = int(input())

# DP 배열 선언
t = [0 for _ in range(36)]
t[0] = 1

# DP 배열 채우기
for i in range(1, 36):
    for j in range(0, i):
        t[i] += t[j] * t[i-1-j]

# 출력부
print(t[n])