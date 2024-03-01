from collections import deque

def complete_time(P, S):
    result = (100-P) // S
    if (100-P) % S: result += 1
    
    return result

def solution(progresses, speeds):
    answer = []
    
    queue = deque()    
    for i in range(len(progresses)):
        queue.append((progresses[i], speeds[i]))
        
    time = complete_time(progresses[0], speeds[0])
    result = 0
    while queue:
        p, s = queue.popleft()
        value = s*time
        
        if p+value >= 100:
            result += 1
            continue
        time = complete_time(p, s)
        answer.append(result)
        result = 1
    
    answer.append(result)
    return answer