# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 선언
INF = -100001
DP = [[INF for _ in range(M)] for _ in range(N)]

# DP 초기값 넣기
Sum = 0
for i in range(M):
    Sum += Map[0][i]
    DP[0][i] = Sum

# DP 배열 채우기(bottom-up)
for X in range(1, N):
    temp1 = [INF for _ in range(M)]
    temp2 = [INF for _ in range(M)]

    # 왼쪽에서 오른쪽으로 가는 경우
    for Y in range(M):
        if Y == 0: temp1[Y] = Map[X][Y] + DP[X-1][Y]
        else: temp1[Y] = Map[X][Y] + max(DP[X-1][Y], temp1[Y-1])

    # 오른쪽에서 왼쪽으로 가는 경우
    for Y in range(M-1, -1, -1):
        if Y == M-1: temp2[Y] = Map[X][Y] + DP[X-1][Y]
        else: temp2[Y] = Map[X][Y] + max(DP[X-1][Y], temp2[Y+1])
    
    # 둘이 비교해서 DP 배열 채우기
    for i in range(M):
        DP[X][i] =max(temp1[i], temp2[i])

# 출력부
print(DP[N-1][M-1])