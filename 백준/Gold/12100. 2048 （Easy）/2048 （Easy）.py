# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 최대 숫자 구하는 함수
def findMax(board):
    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, board[i][j])
    
    return result

# 위로 땡김
def Up(board_):
    # 초기값 설정
    board = [arr[:] for arr in board_]
    merged = [[False for _ in range(N)] for _ in range(N)]

    for j in range(N):
        for i in range(N):
            X, Y = i, j
            merge = False
            
            while True:
                X_ = X-1

                # 이동하지 않는 조건
                if X_ < 0 or not board[X][Y] or (board[X_][Y] and (board[X][Y] != board[X_][Y] or merge)) or merged[X_][Y] :
                    merged[X][Y] = merge
                    break

                # 합치기 or 이동하기
                if board[X][Y] == board[X_][Y]: merge = True
                board[X_][Y] = board[X][Y] + board[X_][Y]
                board[X][Y] = 0
                
                # 갈 수 있는만큼 확인
                X = X_
    
    return board

# 아래로 땡김
def Down(board_):
    # 초기값 설정
    board = [arr[:] for arr in board_]
    merged = [[False for _ in range(N)] for _ in range(N)]

    for j in range(N):
        for i in range(N-1, -1, -1):
            X, Y = i, j
            merge = False
            
            while True:
                X_ = X+1

                # 이동하지 않는 조건
                if X_ == N or not board[X][Y] or (board[X_][Y] and (board[X][Y] != board[X_][Y] or merge)) or merged[X_][Y] :
                    merged[X][Y] = merge
                    break

                # 합치기 or 이동하기
                if board[X][Y] == board[X_][Y]: merge = True
                board[X_][Y] = board[X][Y] + board[X_][Y]
                board[X][Y] = 0
                
                # 갈 수 있는만큼 확인
                X = X_

    return board

# 왼쪽으로 땡김
def Left(board_):
    # 초기값 설정
    board = [arr[:] for arr in board_]
    merged = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            X, Y = i, j
            merge = False
            
            while True:
                Y_ = Y-1

                # 이동하지 않는 조건
                if Y_ < 0 or not board[X][Y] or (board[X][Y_] and (board[X][Y] != board[X][Y_] or merge)) or merged[X][Y_] :
                    merged[X][Y] = merge
                    break

                # 합치기 or 이동하기
                if board[X][Y] == board[X][Y_]: merge = True
                board[X][Y_] = board[X][Y] + board[X][Y_]
                board[X][Y] = 0
                
                # 갈 수 있는만큼 확인
                Y = Y_
    
    return board

# 오른쪽으로 땡김
def Right(board_):
    # 초기값 설정
    board = [arr[:] for arr in board_]
    merged = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N-1, -1, -1):
            X, Y = i, j
            merge = False
            
            while True:
                Y_ = Y+1

                # 이동하지 않는 조건
                if Y_ == N or not board[X][Y] or (board[X][Y_] and (board[X][Y] != board[X][Y_] or merge)) or merged[X][Y_] :
                    merged[X][Y] = merge
                    break

                # 합치기 or 이동하기
                if board[X][Y] == board[X][Y_]: merge = True
                board[X][Y_] = board[X][Y] + board[X][Y_]
                board[X][Y] = 0
                
                # 갈 수 있는만큼 확인
                Y = Y_

    return board
               
# DFS
def DFS(count, board):
    if count == 5: return findMax(board)

    # 초기값 설정
    result = 0

    # 다음 탐색
    for i in range(4):
        temp = [row[:] for row in board] # backtracking
        if i == 0: result = max(result, DFS(count+1, Up(temp)))
        if i == 1: result = max(result, DFS(count+1, Down(temp)))
        if i == 2: result = max(result, DFS(count+1, Left(temp)))
        if i == 3: result = max(result, DFS(count+1, Right(temp)))
    
    return result

print(DFS(0, Map))