from collections import deque
T = int(input())

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

for test_case in range(1,T+1):
    l = int(input())
    startX, startY = map(int,input().split())
    targetX, targetY = map(int,input().split())
    queue = deque()
    visited = [[0 for _ in range(l)] for _ in range(l)]
    
    queue.append([startX,startY])
    
    while queue:
        temp = queue.popleft()
        X = temp[0]
        Y = temp[1]
        
        # 도착
        if X == targetX and Y == targetY:
            print(visited[X][Y])
            break
        
        for i in range(8):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            # 보내지 못하는 경우를 조건으로 구현
            if X_ >= 0 and X_ < l and Y_ >= 0 and Y_ < l and not visited[X_][Y_]:
                visited[X_][Y_] = visited[X][Y] + 1
                queue.append([X_,Y_])