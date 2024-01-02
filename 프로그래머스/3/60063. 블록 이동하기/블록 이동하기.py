from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    visited = [[[[False for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    queue = deque([(0, 0, 0, 1, False, 0)])
    
    while queue:
        X1, Y1, X2, Y2, vertical, time = queue.popleft()
        
        if (X1 == N-1 and Y1 == N-1) or (X2 == N-1 and Y2 == N-1):
            answer = time
            break
        
        for rotation in range(2):
            if not rotation:
                for i in range(4):
                    X1_ = X1 + dx[i]
                    Y1_ = Y1 + dy[i]
                    X2_ = X2 + dx[i]
                    Y2_ = Y2 + dy[i]

                    if X1_ < 0 or X1_ >= N or Y1_ < 0 or Y1_ >= N: continue
                    if X2_ < 0 or X2_ >= N or Y2_ < 0 or Y2_ >= N: continue
                    if board[X1_][Y1_] or board[X2_][Y2_]: continue
                    if visited[X1_][Y1_][X2_][Y2_]: continue

                    visited[X1_][Y1_][X2_][Y2_] = True

                    queue.append((X1_, Y1_, X2_, Y2_, vertical, time+1))
            
            else:
                if vertical:
                    for i in range(4):
                        if i == 0: # 1이 축, 왼쪽으로 회전
                            X1_, Y1_, X2_, Y2_ = X1, Y1-1, X1, Y1

                            if Y1-1 < 0: continue
                            if board[X1+1][Y1-1]: continue
                            
                        if i == 1: # 1이 축, 오른쪽으로 회전
                            X1_, Y1_, X2_, Y2_ = X1, Y1, X1, Y1+1

                            if Y1+1 >= N: continue
                            if board[X1+1][Y1+1]: continue
                        
                        if i == 2: # 2가 축, 왼쪽으로 회전
                            X1_, Y1_, X2_, Y2_ = X2, Y2-1, X2, Y2

                            if Y2-1 < 0: continue
                            if board[X2-1][Y2-1]: continue
                            
                        if i == 3: # 2가 축, 오른쪽으로 회전
                            X1_, Y1_, X2_, Y2_ = X2, Y2, X2, Y2+1

                            if Y2+1 >= N: continue
                            if board[X2-1][Y2+1]: continue
                        
                        if board[X1_][Y1_] or board[X2_][Y2_]: continue
                        if visited[X1_][Y1_][X2_][Y2_]: continue

                        visited[X1_][Y1_][X2_][Y2_] = True

                        queue.append((X1_, Y1_, X2_, Y2_, False, time+1))
                    
                else:
                    for i in range(4):
                        if i == 0: # 1이 축, 위로 회전
                            X1_, Y1_, X2_, Y2_ = X1-1, Y1, X1, Y1

                            if X1-1 < 0: continue
                            if board[X1-1][Y1+1]: continue
                            
                        if i == 1: # 1이 축, 아래로 회전
                            X1_, Y1_, X2_, Y2_ = X1, Y1, X1+1, Y1

                            if X1+1 >= N: continue
                            if board[X1+1][Y1+1]: continue
                            
                        if i == 2: # 2가 축, 위로 회전
                            X1_, Y1_, X2_, Y2_ = X2-1, Y2, X2, Y2

                            if X2-1 < 0: continue
                            if board[X2-1][Y2-1]: continue
                        
                        if i == 3: # 2가 축, 아래로 회전
                            X1_, Y1_, X2_, Y2_ = X2, Y2, X2+1, Y2

                            if X2+1 >= N: continue
                            if board[X2+1][Y2-1]: continue

                        if board[X1_][Y1_] or board[X2_][Y2_]: continue
                        if visited[X1_][Y1_][X2_][Y2_]: continue

                        visited[X1_][Y1_][X2_][Y2_] = True

                        queue.append((X1_, Y1_, X2_, Y2_, True, time+1))
                        
    return answer