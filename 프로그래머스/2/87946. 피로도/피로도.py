def solution(k, dungeons):
    answer = -1
    
    # 초기값 선언
    N = len(dungeons)
    visited = [False for _ in range(N+1)]
    
    def DFS(idx, sleepness):
        # 탐색 불가 조건
        if sleepness < dungeons[idx-1][0]: return 0
        if visited[idx]: return 0
        
        # 탐색 및 다음 탐색
        result = 0
        visited[idx] = True
        for node_ in range(1, N+1): result = max(result, 1+DFS(node_, sleepness - dungeons[idx-1][1]))
        visited[idx] = False
        
        return result
    
    for start in range(1, N+1): answer = max(answer, DFS(start, k))
    return answer