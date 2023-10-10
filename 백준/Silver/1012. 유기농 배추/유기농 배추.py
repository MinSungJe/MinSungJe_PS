import sys
sys.setrecursionlimit(10**6)
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(X,Y):
    # 탐색 불가 조건: 배열이 넘어감
    if X < 0 or X >= M or Y < 0 or Y >= N: return
    # 탐색 불가 조건: 배추가 아님
    if farm[X][Y] == 0: return
    # 탐색 불가 조건: 이미 탐색한 배추임
    if visited[X][Y]: return

    # 방문 처리
    visited[X][Y] = True

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        dfs(X_, Y_)


for test_case in range(1,T+1):
    M, N, K = map(int, input().split())


    farm = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    result = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        farm[X][Y] = 1
    
    for i in range(M):
        for j in range(N):
            # X, Y 전체 탐색
            if farm[i][j] == 1 and not visited[i][j]:
                result += 1
                dfs(i,j)

    print(result)