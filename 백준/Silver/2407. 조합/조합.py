# 입력부
n, m = map(int, input().split())

# 팩토리얼 계산
factorial = [1 for _ in range(101)]
for i in range(1, 101): factorial[i] = factorial[i-1] * i

# 조합 계산
answer = int(factorial[n] // (factorial[n-m] * factorial[m]))
print(answer)