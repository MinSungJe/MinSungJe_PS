def solution(numbers, target):
    def DFS(idx, number):
        if idx == len(numbers):
            if number == target: return 1
            else: return 0
        
        result = 0
        for m in (1, -1):
            result += DFS(idx+1, number + (m*numbers[idx]))
        
        return result
        
    answer = DFS(0, 0)
    
    return answer