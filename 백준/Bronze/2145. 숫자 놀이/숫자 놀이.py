# TC
while True:
    # 입력부
    N = int(input())
    if N == 0: break

    # 자릿수 줄이기
    while N // 10 > 0:
        value = 0
        for digit in list(str(N)): value += int(digit)
        N = value
    
    # 출력부
    print(N)