# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N = map(int, input().split())

# 결과값 미리 그리기
Map = [[1 for _ in range(M)] for _ in range(M)]

# 추가할 값 구하는 함수
def get_value(idx):
    if value[0] - (idx+1) >= 0: return 0
    if (value[0]+value[1]) - (idx+1) >= 0: return 1
    return 2

# 값 추가
for _ in range(N):
    value = list(map(int, input().split()))
    idx = 0
    while idx < (2*M-1):
        idx_value = get_value(idx)
        if idx < M-1:
            x = (M-1)-idx
            Map[x][0] += idx_value            
        if idx >= M-1:
            y = idx-(M-1)
            Map[0][y] += idx_value
        idx += 1

# 배열을 돌며 최댓값 갱신
for x in range(1, M):
    for y in range(1, M):
        min_value = min(x, y)
        Map[x][y] = max(Map[0][y], Map[x][0], Map[x-min_value][y-min_value])

# 출력부
for i in range(M): print(*Map[i])