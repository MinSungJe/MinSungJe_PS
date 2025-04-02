# 입력부
N = int(input())
A = list(map(int, input().split()))

# 투 포인터
l = 0
r = N-1
INF = 200000001
min_value = INF
result = INF
while l < r:
    value = A[l] + A[r]

    # 0이랑 가까운 값일 경우 최신화
    if abs(value) < min_value:
        min_value = abs(value)
        result = value

    if value > 0:
        r -= 1
    if value == 0:
        break
    if value < 0:
        l += 1

# 출력부
print(result)