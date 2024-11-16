# 입력부
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 유클리드 호제법
def GCD(A, B):
    r = A % B
    while r > 0:
        A = B
        B = r
        r = A % B
    return B

# 최대공약수 계산
A_value = 1
B_value = 1
for a in A: A_value *= a
for b in B: B_value *= b
result = GCD(A_value, B_value)

# 출력부
if result // 1000000000: print(f"{result % 1000000000:09d}")
else: print(result)