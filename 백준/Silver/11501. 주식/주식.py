# TC
T = int(input())
for test_case in range(T):
    # 입력부
    N = int(input())
    numbers = list(map(int, input().split()))

    # 뒤에서부터 둘러보기
    result = 0
    max_value = 0
    for i in range(N-1, -1, -1):
        if max_value < numbers[i]:
            max_value = numbers[i]
        else: result += max_value - numbers[i]

    # 출력부
    print(result)