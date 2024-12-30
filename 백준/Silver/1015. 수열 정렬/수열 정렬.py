# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 초기값 선언
idx = 0
value = 1
P = [0 for _ in range(N)]

# P 수열 만들기
while value <= 1000:
    for i in range(N):
        if numbers[i] != value: continue
        P[i] = idx
        idx += 1
    value += 1

# 출력부
print(*P)