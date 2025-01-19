# 입력부
A, B = map(int, input().split(':'))

# 최대공약수 구하는 함수
def getGCD(a, b):
    while b > 0: a, b = b, a % b
    return a

# 함수 호출 및 출력부
gcd = getGCD(A, B)
print(f"{A//gcd}:{B//gcd}")