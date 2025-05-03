# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 늑대 근처에 양이 있는지 확인
result = True
for x in range(R):
    for y in range(C):
        if Map[x][y] == 'W':
            for i in range(4):
                x_, y_ = x+dx[i], y+dy[i]
                if x_ < 0 or x_ >= R or y_ < 0 or y_ >= C: continue
                if Map[x_][y_] == 'S': result = False

# 결과 출력
print(1 if result else 0)
if result:
    for row in Map: print(''.join(row).replace('.', 'D'))