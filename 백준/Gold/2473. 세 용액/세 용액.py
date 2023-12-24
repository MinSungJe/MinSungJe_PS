# 입력부
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

# 초기값 선언
result = (0, 0, 0)

# 왼쪽 용액을 하나 선점
min_value = 3000000001
for l in range(N-2):
    m = l+1
    r = N-1
    while m < r:
        # 두 포인터
        value = numbers[l] + numbers[m] + numbers[r]

        if abs(value) < min_value:
            result = (numbers[l], numbers[m], numbers[r])
            min_value = abs(value)

        if value < 0: m += 1
        elif value > 0: r -= 1
        else: break
    if value == 0: break

# 출력부
print(*result)