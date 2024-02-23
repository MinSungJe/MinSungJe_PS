def solution(n, computers):
    def DFS(com):
        if visited[com]: return
        
        visited[com] = True
        
        for com_ in range(n):
            if computers[com][com_] and not com == com_: DFS(com_)
    
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1
    
    return answer