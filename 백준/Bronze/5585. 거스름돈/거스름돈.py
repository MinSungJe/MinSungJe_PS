# 입력부
N = int(input())

# 거스름돈 계산
rest = 1000 - N
answer = 0

for unit in (500, 100, 50, 10, 5, 1):
    answer += rest // unit
    rest = rest % unit

# 출력부
print(answer)