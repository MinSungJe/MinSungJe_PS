# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N = map(int, input().split())
value = [1 for _ in range(2*M-1)]
result = [[0 for _ in range(M)] for _ in range(M)]
for _ in range(N):
    value_array = list(map(int, input().split()))
    plus_array = [0 for _ in range(value_array[0])] + [1 for _ in range(value_array[1])] + [2 for _ in range(value_array[2])]

    for i in range(2*M-1):
        value[i] += plus_array[i]

# 배열 채우기
idx = 0
for x in range(M-1, -1, -1):
    result[x][0] = value[idx]
    idx += 1
for y in range(1, M):
    result[0][y] = value[idx]
    idx += 1

# 나머지 배열 채우기
for x in range(1, M):
    for y in range(1, M): result[x][y] = result[0][y]

# 출력부
for i in range(M): print(*result[i])