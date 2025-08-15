while True:
    try:
        # 입력부
        N = int(input())

        # 값 확인하기
        result = 1
        while True:
            if result % N == 0:
                print(len(str(result)))
                break
            result *= 10
            result += 1
        

    except: break