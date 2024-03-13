# 입력부
N = int(input())

# 소수 판정(에라토스테네스의 체)
numbers = list()
sosu = [True for _ in range(N+1)]
sosu[0] = False
sosu[1] = False
for i in range(2, N+1):
    if not sosu[i]: continue
    j = 2
    while i*j <= N:
        sosu[i*j] = False
        j += 1
for i in range(N+1):
    if sosu[i]: numbers.append(i) 

# 누적합 구하기
Sum = [0 for _ in range(len(numbers)+1)]
value = 0
for i in range(1, len(numbers)+1):
    value += numbers[i-1]
    Sum[i] = value

# 투 포인터
result = 0
lp = 0
rp = 1
while lp < rp and rp < len(Sum):
    value = Sum[rp] - Sum[lp]

    if value < N:
        rp += 1
        continue
    if value == N: result += 1
    lp += 1

# 출력부
print(result)