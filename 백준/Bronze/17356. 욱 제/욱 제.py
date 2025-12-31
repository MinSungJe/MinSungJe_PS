# 입력부
a, b = map(int, input().split())
M = (b - a) / 400
answer = 1 / (1+10**M)
print(answer)