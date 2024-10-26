# 빠른 입력
while True:
    letter = input()

    # 종류
    if letter == '*': break

    # D에 따라 유일한지 확인
    N = len(letter)
    result = True
    for D in range(1, N):
        Set = set()
        for i in range(N):
            if i+D >= N: break
            value = f"{letter[i]}{letter[i+D]}"
            if Set.intersection({value}):
                result = False
                break
            Set.add(value)
    
    # 출력부
    print(f"{letter} is surprising." if result else f"{letter} is NOT surprising.")