# 입력부
s, N, K, R1, R2, C1, C2 = map(int, input().split())

# 프랙탈의 해당 부분 구하는 함수
def fractal(X, Y, L):
    # 정복 완료
    if L == 1: return 0

    # 분할
    seperate = L//N
    X_part = X // seperate
    Y_part = Y // seperate

    # 중앙값 구하기
    padding = (N-K)//2
    # 검정이 칠해지는 경우
    if padding <= X_part < padding+K and padding <= Y_part < padding+K: return 1
    else: return fractal(X-(X_part*seperate), Y-(Y_part*seperate), seperate)


# 한 변의 길이 구하기
L = N**s

# 함수 호출 및 출력부
for X in range(R1, R2+1):
    for Y in range(C1, C2+1):
        
        result = fractal(X, Y, L)
        print(result, end='')
    print()
