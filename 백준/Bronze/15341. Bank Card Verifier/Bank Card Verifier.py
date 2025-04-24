while True:
    # 입력부
    first, second, third, fourth = map(str, input().split())

    # 종료
    if first == "0000" and second == "0000" and third == "0000" and fourth == "0000": break

    # 카드 검사
    result = 0
    for number in (first, second, third, fourth):
        for idx in range(4):
            value = int(number[idx])
            if idx == 1 or idx == 3:
                result += value
                continue

            value *= 2
            if value > 9: value -= 9
            result += value
    
    # 출력부
    print("Yes" if not result % 10 else "No")