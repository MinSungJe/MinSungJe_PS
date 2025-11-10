def solution(brown, yellow):
    answer = []
    
    for y in range(1, yellow+1):
        if yellow % y != 0: continue
        x = yellow // y
        
        if (x+2) * (y+2) - (x*y) == brown:
            answer.append(x+2)
            answer.append(y+2)
            break
    
    return answer