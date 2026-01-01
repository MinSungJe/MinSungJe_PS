# 입력부
N = int(input())
divider = 2

# 소인수분해 알고리즘
while N > 1:
    if N % divider == 0:
        N //= divider
        print(divider)
        continue

    divider += 1