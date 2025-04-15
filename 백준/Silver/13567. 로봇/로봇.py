# 입력부
M, n = map(int, input().split())
cmd = [input().split() for _ in range(n)]

# 초기값 선언
X, Y, d = 0, 0, 2
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

# 로봇 이동
result = True
for act, value in cmd:
    # 움직임 명령
    if act == 'MOVE':
        X += dx[d] * int(value)
        Y += dy[d] * int(value)

        # 유효하지 않은 값인지 검사
        if X < 0 or X > M or Y < 0 or Y > M:
            result = False
            break
    
    # 돌 때 명령
    if act == 'TURN':
        if value == '0': d = (d+1) % 4
        if value == '1': d = (d+3) % 4

# 출력부
if result: print(X, Y)
else: print(-1)