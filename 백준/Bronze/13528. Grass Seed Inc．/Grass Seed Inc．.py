# 입력부
C = float(input())
L = int(input())

# 넓이 계산
result = 0
for _ in range(L):
    w, l = map(float, input().split())
    result += w * l

# 출력부
print(result * C)