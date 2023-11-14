# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
sumMap = [[0 for _ in range(N+1)] for _ in range(N+1)]

# 누적합 배열 채우기
for i in range(1, N+1):
    for j in range(1, N+1):
        sumMap[i][j] = sumMap[i-1][j] + sumMap[i][j-1] - sumMap[i-1][j-1] + Map[i-1][j-1]

# 출력부
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = sumMap[x2][y2] - sumMap[x1-1][y2] - sumMap[x2][y1-1] + sumMap[x1-1][y1-1]
    print(result)