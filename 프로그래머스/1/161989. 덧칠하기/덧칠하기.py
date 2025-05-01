def solution(n, m, section):
    answer = 0
    
    last_paint = -1
    index = 0
    
    for tile in range(1, n+1):
        if index == len(section) or tile != section[index]: continue
        if last_paint == -1 or last_paint + m <= tile:
            answer += 1
            last_paint = tile
        index += 1

    return answer