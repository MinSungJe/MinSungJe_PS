# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

# 모래 이동
def wind(x, y, D):
    # 초기값 선언
    result = 0
    X, Y = x+dx[D], y+dy[D]
    value = Map[X][Y]
    sand = [int(value * (5/100)), int(value * (10/100)), int(value * (7/100)), int(value * (2/100)), int(value * (1/100))]

    if D == 0:
        # 5%
        if Y-2 >= 0: Map[X][Y-2] += sand[0]
        else: result += sand[0]
        Map[X][Y] -= sand[0]

        # 10%
        if X-1 >= 0 and Y-1 >= 0: Map[X-1][Y-1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]
        if X+1 < N and Y-1 >= 0: Map[X+1][Y-1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]

        # 7%
        if X-1 >= 0: Map[X-1][Y] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]
        if X+1 < N: Map[X+1][Y] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]

        # 2%
        if X-2 >= 0: Map[X-2][Y] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]
        if X+2 < N: Map[X+2][Y] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]

        # 1%
        if X-1 >= 0 and Y+1 < N: Map[X-1][Y+1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]
        if X+1 < N  and Y+1 < N: Map[X+1][Y+1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]

        left_sand = Map[X][Y]
        if Y-1 >= 0: Map[X][Y-1] += left_sand
        else: result += left_sand
        Map[X][Y] = 0

    if D == 1:
        # 5%
        if X+2 < N: Map[X+2][Y] += sand[0]
        else: result += sand[0]
        Map[X][Y] -= sand[0]

        # 10%
        if X+1 < N and Y-1 >= 0: Map[X+1][Y-1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]
        if X+1 < N and Y+1 < N: Map[X+1][Y+1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]

        # 7%
        if Y-1 >= 0: Map[X][Y-1] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]
        if Y+1 < N: Map[X][Y+1] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]

        # 2%
        if Y-2 >= 0: Map[X][Y-2] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]
        if Y+2 < N: Map[X][Y+2] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]

        # 1%
        if X-1 >= 0 and Y-1 >= 0: Map[X-1][Y-1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]
        if X-1 >= 0  and Y+1 < N: Map[X-1][Y+1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]

        left_sand = Map[X][Y]
        if X+1 < N: Map[X+1][Y] += left_sand
        else: result += left_sand
        Map[X][Y] = 0
    
    if D == 2:
        # 5%
        if Y+2 < N: Map[X][Y+2] += sand[0]
        else: result += sand[0]
        Map[X][Y] -= sand[0]

        # 10%
        if X-1 >= 0 and Y+1 < N: Map[X-1][Y+1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]
        if X+1 < N and Y+1 < N: Map[X+1][Y+1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]

        # 7%
        if X-1 >= 0: Map[X-1][Y] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]
        if X+1 < N: Map[X+1][Y] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]

        # 2%
        if X-2 >= 0: Map[X-2][Y] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]
        if X+2 < N: Map[X+2][Y] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]

        # 1%
        if X-1 >= 0 and Y-1 >= 0: Map[X-1][Y-1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]
        if X+1 < N  and Y-1 >= 0: Map[X+1][Y-1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]

        left_sand = Map[X][Y]
        if Y+1 < N: Map[X][Y+1] += left_sand
        else: result += left_sand
        Map[X][Y] = 0

    if D == 3:
        # 5%
        if X-2 >= 0: Map[X-2][Y] += sand[0]
        else: result += sand[0]
        Map[X][Y] -= sand[0]

        # 10%
        if X-1 >= 0 and Y-1 >= 0: Map[X-1][Y-1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]
        if X-1 >= 0 and Y+1 < N: Map[X-1][Y+1] += sand[1]
        else: result += sand[1]
        Map[X][Y] -= sand[1]

        # 7%
        if Y-1 >= 0: Map[X][Y-1] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]
        if Y+1 < N: Map[X][Y+1] += sand[2]
        else: result += sand[2]
        Map[X][Y] -= sand[2]

        # 2%
        if Y-2 >= 0: Map[X][Y-2] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]
        if Y+2 < N: Map[X][Y+2] += sand[3]
        else: result += sand[3]
        Map[X][Y] -= sand[3]

        # 1%
        if X+1 < N and Y-1 >= 0: Map[X+1][Y-1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]
        if X+1 < N  and Y+1 < N: Map[X+1][Y+1] += sand[4]
        else: result += sand[4]
        Map[X][Y] -= sand[4]

        left_sand = Map[X][Y]
        if X-1 >= 0: Map[X-1][Y] += left_sand
        else: result += left_sand
        Map[X][Y] = 0

    return result


# 토네이도
pos = [N//2, N//2, 0]
result = 0
for i in range(1, N+1):
    for _ in range(2):
        for _ in range(i):
            result += wind(pos[0], pos[1], pos[2])
            pos[0], pos[1] = pos[0]+dx[pos[2]], pos[1]+dy[pos[2]]
        if i == N: break
        pos[2] = (pos[2]+1)%4

# 출력부
print(result)