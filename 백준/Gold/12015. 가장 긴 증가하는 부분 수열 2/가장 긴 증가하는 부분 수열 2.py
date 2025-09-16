# 입력부
N = int(input())
A = list(map(int, input().split()))

# 초기값 선언
D = [0 for _ in range(N)]
LIS = [0]

for i in range(N):
    value = A[i]

    # lower_bound
    l = 0
    r = len(LIS)
    while l < r:
        mid = (l+r) // 2
        if LIS[mid] < value: l = mid + 1
        else: r = mid

    if r >= len(LIS): LIS.append(value)
    else: LIS[r] = value
    D[i] = r

# 출력부
answer = max(D)
print(answer)