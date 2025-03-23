# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, R = map(int, input().split())
rice = [list(map(int, input().split())) for _ in range(N)]

# 안에 들어왔는지 확인하는 함수
def isInWok(X, Y, WX, WY):
    return getDistance(X, Y, WX, WY) <= R**2

# 거리제곱 구하는 함수
def getDistance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

# 완전 탐색
result = [0, 0, 0]
for X in range(-100, 101):
    for Y in range(-100, 101):
        value = 0
        for i in range(N):
            if isInWok(rice[i][0], rice[i][1], X, Y): value += 1
        if result[2] < value: result[0], result[1], result[2] = X, Y, value

# 출력부
print(result[0], result[1])