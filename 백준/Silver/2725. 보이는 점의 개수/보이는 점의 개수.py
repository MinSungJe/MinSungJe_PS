# 유클리드 호제법
def GCD(A, B):
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B
    return B

# 모든 경우 구하기
answer = [0 for _ in range(1001)]
answer[1] = 3
for x in range(2, 1001):
    result = 0
    for y in range(1, x):
        if GCD(x, y) == 1: result += 1
    answer[x] = result * 2 + answer[x-1]

# TC
C = int(input())
for _ in range(C):
    # 입력부
    N = int(input())
    
    # 출력부
    print(answer[N])