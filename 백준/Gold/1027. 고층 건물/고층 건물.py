# 입력부
N = int(input())
buildings = list(map(int, input().split()))

# 일차함수식 기울기, y절편 구하기
def get_expression(X1, Y1, X2, Y2):
    a = (Y1- Y2)/(X1- X2)
    b = Y1 - (a*X1)

    return a, b

# 초기값 선언
result = [0 for _ in range(N)]

# 빌딩 고르기
for X1 in range(N):
    for X2 in range(N):
        if X1 == X2: continue
        canSee = True
        Y1, Y2 = buildings[X1], buildings[X2]

        # 일차함수식 구하기
        A, B = get_expression(X1, Y1, X2, Y2)

        # 둘 사이의 빌딩 확인
        if X1 < X2:
            for X3 in range(X1+1, X2):
                if A*X3+B <= buildings[X3]:
                    canSee = False
                    break
        else:
            for X3 in range(X2+1, X1):
                if A*X3+B <= buildings[X3]:
                    canSee = False
                    break
        if canSee: result[X1] += 1

# 출력부
print(max(result))