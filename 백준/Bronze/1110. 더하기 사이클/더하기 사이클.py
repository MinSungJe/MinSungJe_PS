# 입력부
N = int(input())

# 사이클 개수 구하기
result = 0
temp = N
while True:
    A = temp%10
    B = ((temp//10) + (temp%10)) % 10
    temp = 10*A + B
    result += 1

    if temp == N: break

# 출력부
print(result)