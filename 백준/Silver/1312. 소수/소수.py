# 입력부
A, B, N = map(int, input().split())

# 나눗셈
for _ in range(N):
    A = (A % B) * 10
    result = A//B

# 출력부
print(result)