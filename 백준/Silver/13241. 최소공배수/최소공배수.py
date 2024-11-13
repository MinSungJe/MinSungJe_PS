# 입력부
A, B = map(int, input().split())

# 유클리드 호제법
a, b = A, B
r = a % b
while r > 0:
    a = b
    b = r
    r = a % b
GCD = b
LCM = (A*B) // GCD

# 출력부
print(LCM)