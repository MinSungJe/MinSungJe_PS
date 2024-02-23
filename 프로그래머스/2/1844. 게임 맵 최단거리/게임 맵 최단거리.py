from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 1)])
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    while queue:
        X, Y, count = queue.popleft()
        
        if X < 0 or X >= n or Y < 0 or Y >= m: continue
        if not maps[X][Y]: continue
        if visited[X][Y]: continue
        
        if X == n-1 and Y == m-1:
            answer = count
            break
        visited[X][Y] = True
        
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_, count+1))
    
    return answer