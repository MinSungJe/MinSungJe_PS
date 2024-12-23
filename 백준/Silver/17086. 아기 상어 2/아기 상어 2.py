# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 두 점 사이의 거리 구하는 함수
def getDistance(x1, y1, x2, y2):
    return max(abs(x1-x2), abs(y1-y2))

# 한 점에서 안전거리 구하는 함수
def getSafeDistance(x, y):
    result = 2501
    for babyX, babyY in baby:
        result = min(result, getDistance(x, y, babyX, babyY))
    
    return result

# 아기 상어 위치 저장
baby = list()
for x in range(N):
    for y in range(M):
        if Map[x][y] == 1: baby.append((x, y))

# 안전거리 최댓값 구하기
result = 0
for x in range(N):
    for y in range(M):
        result = max(result, getSafeDistance(x, y))

# 출력부
print(result)