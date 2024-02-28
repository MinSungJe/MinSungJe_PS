# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
heartX, heartY = -1, -1
bottomX, bottomY = 0, 0
result = [0, 0, 0, 0, 0]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 머리 위치를 통해 심장위치 찾기
for i in range(N):
    for j in range(N):
        if Map[i][j] == '*':
            heartX, heartY = i+1, j
            break
    if heartX != -1: break

# 왼쪽 팔
for i in range(heartY-1, -1, -1):
    if Map[heartX][i] == '_': break
    result[0] += 1

# 오른쪽 팔
for i in range(heartY+1, N):
    if Map[heartX][i] == '_': break
    result[1] += 1

# 허리
for i in range(heartX+1, N):
    if Map[i][heartY] == '_':
        bottomX, bottomY = i, heartY
        break
    result[2] += 1

# 왼쪽 다리
for i in range(bottomX, N):
    if Map[i][bottomY-1] == '_': break
    result[3] += 1

# 오른쪽 다리
for i in range(bottomX, N):
    if Map[i][bottomY+1] == '_': break
    result[4] += 1

# 출력부
print(heartX+1, heartY+1)
print(*result)