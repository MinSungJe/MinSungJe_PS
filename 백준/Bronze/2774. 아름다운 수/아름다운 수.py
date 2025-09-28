# 입력부
T = int(input())

# 테스트 케이스
for _ in range(T):
    X = input()
    numbers = [0 for _ in range(10)]

    for digit in X: numbers[int(digit)] = 1

    # 출력부
    answer = sum(numbers)
    print(answer)