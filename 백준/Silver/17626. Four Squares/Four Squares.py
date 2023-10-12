# 입력부
n = int(input())

# 제곱수인지 확인하는 함수
def isDouble(N):
    if N**(1/2) % 1 == 0: return True
    else: return False

# 결과 계산하는 함수
def sol(N):
    if isDouble(N): return 1

    for i in range(1,224):
        Num = N - (i*i)
        if Num < 0: break
        if isDouble(Num): return 2

    for i in range(1,224):
        for j in range(1,224):
            Num = N - (i*i) - (j*j)
            if Num < 0: break
            if isDouble(Num): return 3
    return 4

# 출력부
print(sol(n))