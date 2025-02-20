# 입력부
T = int(input())
for _ in range(T):
    math = input().split()
    number = float(math[0])

    # 계산
    for i in range(1, len(math)):
        if math[i] == '@': number *= 3
        if math[i] == '%': number += 5
        if math[i] == '#': number -= 7

    # 출력부
    print(f"{number:.2f}")