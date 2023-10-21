# 입력부
N = int(input())

# 초기값 설정
Stars = [[' ' for _ in range(2*N - 1)] for _ in range(N)]

# 분할정복 알고리즘
def Star(X, Y, length):
    global Stars

    # 분할 완료
    if length == 3:
        Stars[X][Y] = '*'
        Stars[X+1][Y-1] = '*'
        Stars[X+1][Y+1] = '*'
        Stars[X+2][Y-2] = '*'
        Stars[X+2][Y-1] = '*'
        Stars[X+2][Y] = '*'
        Stars[X+2][Y+1] = '*'
        Stars[X+2][Y+2] = '*'
        return

    # 분할
    for X_, Y_ in [[X,Y], [X+length//2, Y-length//2], [X+length//2, Y+length//2]]:
        Star(X_, Y_, length//2)

# 출력부
Star(0,N-1,N)
for s in Stars: print("".join(s))