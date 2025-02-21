# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 성규와 교수 위치 확인
pos2 = {'x': 0, 'y': 0}
pos5 = {'x': 0, 'y': 0}
for x in range(N):
    for y in range(N):
        if Map[x][y] == 2: pos2['x'], pos2['y'] = x, y
        if Map[x][y] == 5: pos5['x'], pos5['y'] = x, y

# 위치 확인 함수
def getDistance(x1, y1, x2, y2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2)

# 둘 사이 학생이 몇 있는지 확인 함수
def getBetweenStudent(x1, y1, x2, y2):
    result = 0
    minX, maxX = min(x1, x2), max(x1, x2)
    minY, maxY = min(y1, y2), max(y1, y2)
    for x in range(minX, maxX+1):
        for y in range(minY, maxY+1):
            if Map[x][y] == 1: result += 1
    return result

# 함수 호출
result = True
distance = getDistance(pos2['x'], pos2['y'], pos5['x'], pos5['y'])
betweenStudent = getBetweenStudent(pos2['x'], pos2['y'], pos5['x'], pos5['y'])
if distance < 5: result = False
if betweenStudent < 3: result = False

# 출력부
print(1 if result else 0)