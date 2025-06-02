# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
A, B = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda x: (x[0], x[1]))

# 점 위치 기록
pointPos = dict()
for X, Y in points:
    if pointPos.get(X) == None: pointPos[X] = {Y}
    else: pointPos[X].add(Y)

# 점 마다 직사각형이 될 수 있는 지 확인
result = 0
for X, Y in points:
    if pointPos.get(X+A) == None: continue
    if Y+B not in pointPos[X]: continue
    if Y not in pointPos[X+A]: continue
    if Y+B not in pointPos[X+A]: continue
    result += 1

# 출력부
print(result)