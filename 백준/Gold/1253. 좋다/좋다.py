# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 숫자 정렬
numbers.sort()

# 모든 수에 대해 탐색
result = 0
for i in range(N):
    target = numbers[i]

    # 투 포인터
    p1, p2 = 0, N-1

    while p1 < p2:
        if p1 == i:
            p1 += 1
            continue
        if p2 == i:
            p2 -= 1
            continue
        value = numbers[p1]+numbers[p2]

        if value == target:
            result += 1
            break
        if value < target: p1 += 1
        if value > target: p2 -= 1

# 출력부
print(result)