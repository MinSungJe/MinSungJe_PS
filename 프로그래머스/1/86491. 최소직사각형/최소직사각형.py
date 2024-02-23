def solution(sizes):
    width = list()
    height = list()
    
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    
    answer = max(width) * max(height)
    return answer