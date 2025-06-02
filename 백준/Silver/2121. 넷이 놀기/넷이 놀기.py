# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
A, B = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda x: (x[0], x[1]))

# 점 위치 기록
pointPos = set()
for X, Y in points: pointPos.add((X, Y))

# 점 마다 직사각형이 될 수 있는 지 확인
result = 0
for X, Y in points:
    if (X, Y+B) not in pointPos: continue
    if (X+A, Y) not in pointPos: continue
    if (X+A, Y+B) not in pointPos: continue
    result += 1

# 출력부
print(result)