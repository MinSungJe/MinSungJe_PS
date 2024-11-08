# TC
T = int(input())

# 전역변수 선언
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)

# 방향전환
def changeDir(current, direction):
    if direction == 'L':
        return (current + 3) % 4
    if direction == 'R':
        return (current + 1) % 4

for test_case in range(1, T+1):
    # 입력부
    cmds = input()
    direction = 0
    pos = [0, 0]
    north, south, west, east = 0, 0, 0, 0

    # 거북이 이동
    for cmd in cmds:
        if cmd == 'F':
            pos[0] += dx[direction]
            pos[1] += dy[direction]
        if cmd == 'B':
            pos[0] -= dx[direction]
            pos[1] -= dy[direction]
        if cmd == 'L' or cmd == 'R':
            direction = changeDir(direction, cmd)
        
        north = min(north, pos[0])
        south = max(south, pos[0])
        west = min(west, pos[1])
        east = max(east, pos[1])
        
    # 출력부
    result = (south-north)*(east-west)
    print(result)