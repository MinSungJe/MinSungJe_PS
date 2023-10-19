from collections import deque

def solution(x, y, n):
    answer = -1
    queue = deque([(x,0)])
    visited = [False for _ in range(1000001)]
    
    while queue:
        X, count = queue.popleft()
        
        if X == y:
            answer = count
            break
        
        if X > y: continue
        if visited[X]: continue
        
        visited[X] = True
        
        for X_ in [X+n, 2*X, 3*X]:
            queue.append((X_,count+1))
    
    return answer