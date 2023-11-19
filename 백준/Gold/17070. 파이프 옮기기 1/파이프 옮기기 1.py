# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# DP Table
DP = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

# DP Table 작성
DP[0][1][0] = 1
for i in range(N):
    for j in range(N):
        # 검사하는 위치가 벽임
        if Map[i][j] == 1: continue

        # 끝이 가로방향
        if j-1 >= 0: # 범위 확인
            DP[i][j][0] += DP[i][j-1][0] # 가로 -> 가로 방향
            DP[i][j][0] += DP[i][j-1][2] # 대각선 -> 가로 방향

        # 끝이 세로방향
        if i-1 >= 0: # 범위 확인
            DP[i][j][1] += DP[i-1][j][1] # 세로 -> 세로 방향
            DP[i][j][1] += DP[i-1][j][2] # 대각선 -> 세로 방향

        # 끝이 대각선방향
        if i-1 >= 0 and j-1 >= 0 and not Map[i-1][j] and not Map[i][j-1]: # 범위 확인
            DP[i][j][2] += DP[i-1][j-1][0] # 가로 -> 대각선 방향
            DP[i][j][2] += DP[i-1][j-1][1] # 세로 -> 대각선 방향
            DP[i][j][2] += DP[i-1][j-1][2] # 대각선 -> 대각선 방향

# 출력부
print(sum(DP[N-1][N-1]))