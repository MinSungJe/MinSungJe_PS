# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
board = list(map(int, input().split()))

# DP Table 생성 및 채우기
DP = [[0 for _ in range(N)] for _ in range(N)]
for gap in range(N):
    for i in range(0, N-gap):
        j = i + gap
        # gap이 0이면 같은 숫자 -> 팰린드롬
        if gap == 0: DP[i][j] = 1
        # gap이 1 또는 2이면 같은지 확인 -> 같으면 팰린드롬
        elif gap == 1 or gap == 2:
            if board[i] == board[j]: DP[i][j] = 1
        else: # gap이 3 이상이면 안쪽이 팰린드롬인지 확인 + 현재 값이 같은지 확인
            if board[i] == board[j]: DP[i][j] = 1 * DP[i+1][j-1]

# 출력부
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(DP[S-1][E-1])