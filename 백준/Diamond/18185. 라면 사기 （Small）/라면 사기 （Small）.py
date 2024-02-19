# 입력부
N = int(input())
factory = list(map(int, input().split())) + [0, 0]

# 1개 구입
def buy_one(idx):
    global result
    result += 3 * factory[idx]

# 2개 구입
def buy_two(idx, m):
    global result
    factory[idx] -= m
    factory[idx+1] -= m
    result += 5 * m

# 3개 구입
def buy_three(idx):
    global result
    m = min(factory[idx:idx+3])
    factory[idx] -= m
    factory[idx+1] -= m
    factory[idx+2] -= m
    result += 7 * m

# 결과값 도출 및 출력
result = 0
for i in range(N):
    if factory[i+1] > factory[i+2]:
        buy_two(i, min(factory[i], factory[i+1]-factory[i+2]))
        buy_three(i)
        buy_one(i)
    else:
        buy_three(i)
        buy_two(i, min(factory[i:i+2]))
        buy_one(i)
print(result)