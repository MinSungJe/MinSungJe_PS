# 입력부
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 출력부
result = sorted(A+B)
print(*result)