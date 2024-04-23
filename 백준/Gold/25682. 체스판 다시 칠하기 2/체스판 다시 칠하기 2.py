# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 다른 부분 파악
Sum1 = [[0 for _ in range(M)] for _ in range(N)] # 왼쪽위 B
Sum2 = [[0 for _ in range(M)] for _ in range(N)] # 왼쪽위 W
for i in range(N):
    for j in range(M):
        if (i+j) % 2 == 0: # 합이 짝수 -> 왼쪽위랑 같은 색깔
            if board[i][j] != 'B': Sum1[i][j] = 1
            else: Sum2[i][j] = 1
        else: # 합이 홀수  -> 왼쪽위랑 다른 색깔
            if board[i][j] != 'W': Sum1[i][j] = 1
            else: Sum2[i][j] = 1

for i in range(N):
    for j in range(M):
        if (i-1) >= 0:
            Sum1[i][j] += Sum1[i-1][j]
            Sum2[i][j] += Sum2[i-1][j]
        if (j-1) >= 0:
            Sum1[i][j] += Sum1[i][j-1]
            Sum2[i][j] += Sum2[i][j-1]
        if (i-1) >= 0 and (j-1) >= 0:
            Sum1[i][j] -= Sum1[i-1][j-1]
            Sum2[i][j] -= Sum2[i-1][j-1]

# 다른 영역(다시 칠해야 하는 영역) 최솟값 구하기
result = N * M
for i in range((K-1), N):
    for j in range((K-1), M):
        value1, value2 = Sum1[i][j], Sum2[i][j]
        if i-K >= 0:
            value1 -= Sum1[i-K][j]
            value2 -= Sum2[i-K][j]
        if j-K >= 0:
            value1 -= Sum1[i][j-K]
            value2 -= Sum2[i][j-K]
        if i-K >= 0 and j-K >= 0:
            value1 += Sum1[i-K][j-K]
            value2 += Sum2[i-K][j-K]
        
        result = min(result, value1, value2)

# 출력부
print(result)