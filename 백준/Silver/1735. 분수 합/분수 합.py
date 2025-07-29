# 유클리드 호제법
def GCD(A, B):
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B
    return B

# 입력부
A, B = map(int, input().split())
C, D = map(int, input().split())

# 분수 계산하기
AC = A*D + B*C
BD = B*D

# 최대공약수 계산하기
gcd = GCD(AC, BD)

# 출력부
print(AC // gcd, BD // gcd)