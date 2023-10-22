# 입력부
N = int(input())

# 초기값 선언
Stars = [[' ' for _ in range(N)] for _ in range(N)]

# 분할정복 선언
def Star(X, Y, length):
    global Stars
    # 정복
    if length == 1:
        Stars[X][Y] = '*'
        return

    # 분할
    for X_ in range(X, X+length, length//3):
        for Y_ in range(Y, Y+length, length//3):
            if X_ == X+length//3 and Y_ == Y+length//3: continue
            Star(X_, Y_, length//3)
        
# 출력부
Star(0,0,N)
for s in Stars:
    print(''.join(s))