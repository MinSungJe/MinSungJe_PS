# 입력부
T = int(input())

for _ in range(T):
    number = int(input())
    result = 0
    
    # 6174가 될때까지 탐색
    while True:
        # 탐색 종료
        if number == 6174:
            break

        # 4자리 숫자 조합해서 가장 큰 수 구하기
        digits = [0, 0, 0, 0]

        digits[0] = number // 1000
        digits[1] = (number % 1000) // 100
        digits[2] = (number % 100) // 10
        digits[3] = number % 10
        
        # 가장 작은 수
        digits.sort()
        min_value = 1000*digits[0] + 100*digits[1] + 10*digits[2] + digits[3]

        # 가장 큰수
        digits.sort(reverse=True)
        max_value = 1000*digits[0] + 100*digits[1] + 10*digits[2] + digits[3]

        # 다음 상태
        number = max_value - min_value
        result += 1
    
    # 출력부
    print(result)