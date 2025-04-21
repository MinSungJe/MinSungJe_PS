# 입력부
W, H, X, Y, P = map(int, input().split())

# 네모 안에 있는지 확인
def check_is_in_square(x, y):
    return (x >= X and x <= X+W) and (y >= Y and y <= Y+H)

# 동그라미 안에 있는지 확인
def check_is_in_round(x, y):
    r = H // 2
    return ((x-X)**2 + (y-(Y+r)) ** 2 <= r**2) or ((x-(X+W))**2 + (y-(Y+r)) ** 2 <= r**2)

# 링크 안에 있는지 확인
def check_is_in_rink(x, y):
    return check_is_in_square(x, y) or check_is_in_round(x, y)

# 링크 안에 있는 선수의 수 확인
result = 0
for _ in range(P):
    x, y = map(int, input().split())
    if check_is_in_rink(x, y): result += 1

# 출력부
print(result)