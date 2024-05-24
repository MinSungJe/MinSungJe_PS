# 입력부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 점수 구하는 함수
def score(arr): return max(arr) - min(arr)

# 최솟값 주어지면 구간 나누는 함수
def divideRange(min_value):
    result = 0
    idx = 0
    gap = 0
    while idx < N:
        gap += 1

        if idx+gap > N: # 끝 도착
            result += 1
            break
        if score(numbers[idx:idx+gap]) <= min_value: continue

        result += 1
        idx = (idx+gap) - 1
        gap = 0

    return result

# 이분 탐색
l = 0
r = 10001
result = 0
while l < r:
    m = (l+r) // 2

    if divideRange(m) <= M:
        result = m
        r = m
    else: l = m+1

# 출력부
print(result)