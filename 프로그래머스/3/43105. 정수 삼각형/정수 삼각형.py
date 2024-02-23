def solution(triangle):
    DP = [[-1 for _ in range(500)] for _ in range(500)]
    
    def DFS(X, Y):
        if X == len(triangle): return 0
        if DP[X][Y] != -1: return DP[X][Y]
        
        result = 0
        for p in (0, 1):
            result = max(result, triangle[X][Y]+DFS(X+1, Y+p))
        DP[X][Y] = result
        return result
        
    answer = DFS(0, 0)
    return answer