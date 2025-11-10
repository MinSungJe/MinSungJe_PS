def solution(board):
    INF = (25 * 25 * 600) + 1
    answer = [INF]
    N = len(board)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[INF, INF] for _ in range(N)] for _ in range(N)]

    def DFS(X, Y, isVertical, value):
        isVerticalIndex = 1 if isVertical else 0

        # 탐색 종료 조건
        if X == N - 1 and Y == N - 1:
            answer[0] = min(answer[0], value)
            return

        # 탐색 불가 조건
        if X < 0 or X >= N or Y < 0 or Y >= N:
            return
        if board[X][Y] == 1:
            return
        if visited[X][Y][isVerticalIndex] <= value:
            return

        # 탐색
        visited[X][Y][isVerticalIndex] = value

        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            if isVertical:
                if i in (0, 1):
                    DFS(X_, Y_, True, value + 100)
                else:
                    DFS(X_, Y_, False, value + 600)
            else:
                if i in (0, 1):
                    DFS(X_, Y_, True, value + 600)
                else:
                    DFS(X_, Y_, False, value + 100)

    # 초기 호출 (가로, 세로 각각 시작)
    DFS(0, 0, True, 0)
    DFS(0, 0, False, 0)
    
    return answer[0]
