# 입력부
N = int(input())
Map = [list(list(input())) for _ in range(N)]
K = int(input())

# 출력부
if K == 1:
    for row in Map: print(''.join(row))

if K == 2:
    for row in Map: print(''.join(row[::-1]))

if K == 3:
    for row in Map[::-1]: print(''.join(row))