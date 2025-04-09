# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 회전 가능 형태 기록
dx = (0, 1, 1)
dy = (1, 1, 0)
rotate = [[0, 1], [0, 1, 2], [1, 2]]

# DP 배열 선언
DP = [[[-1 for _ in range(3)] for _ in range(N)] for _ in range(N)]

# DFS
def DFS(X, Y, pos):
    # 도착
    if X == N-1 and Y == N-1: return 1
    if DP[X][Y][pos] != -1: return DP[X][Y][pos]
    
    # 다음 탐색
    result = 0
    for pos_ in rotate[pos]:
        X_, Y_ = X+dx[pos_], Y+dy[pos_]

        # 이동 불가
        if X_ >= N or Y_ >= N or Map[X_][Y_]: continue
        # 대각선 이동 추가 점검
        if pos_ == 1 and (Map[X_-1][Y_] or Map[X_][Y_-1]): continue

        result += DFS(X_, Y_, pos_)

    # 메모이제이션
    DP[X][Y][pos] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 1, 0)
print(result)