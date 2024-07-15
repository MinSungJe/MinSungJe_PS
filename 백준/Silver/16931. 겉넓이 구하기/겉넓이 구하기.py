# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

result = 0
result += (N*M*2) # 밑면, 윗면 넓이 더하기

# 옆면 넓이 더하기
for i in range(N):
    # 왼쪽에서 바라봄
    prev_value = 0
    for j in range(M):
        value = Map[i][j]
        if prev_value < value: result += (value - prev_value)
        prev_value = value

    # 오른쪽에서 바라봄
    prev_value = 0
    for j in range(M-1, -1, -1):
        value = Map[i][j]
        if prev_value < value: result += (value - prev_value)
        prev_value = value

for j in range(M):
    # 위쪽에서 바라봄
    prev_value = 0
    for i in range(N):
        value = Map[i][j]
        if prev_value < value: result += (value - prev_value)
        prev_value = value
    
    # 아래쪽에서 바라봄
    prev_value = 0
    for i in range(N-1, -1, -1):
        value = Map[i][j]
        if prev_value < value: result += (value - prev_value)
        prev_value = value

# 출력부
print(result)