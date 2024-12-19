# 입력부
N, M = map(int, input().split())
J = int(input())

# 초기값 선언
L = 1
R = L+(M-1)

# 사과 받기
result = 0
for _ in range(J):
    apple = int(input())
    if apple < L:
        value = L-apple
        result += value
        L -= value
        R -= value

    if apple > R:
        value = apple-R
        result += value
        L += value
        R += value

# 출력부
print(result)