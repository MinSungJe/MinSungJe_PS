# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 초기값 선언
max_number = max(numbers)
set_numbers = set(numbers)
result = [0 for _ in range(1000001)]

# 에라토스테네스의 체 적용
for A in numbers:
    for B in range(2*A, max_number+1, A):
        if B in set_numbers:
            result[A] += 1
            result[B] -= 1

# 출력부
answer = list()
for number in numbers:
    answer.append(result[number])
print(*answer)