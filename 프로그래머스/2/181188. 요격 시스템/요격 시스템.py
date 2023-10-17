def solution(targets):
    
    # 배열 정렬
    targets.sort()
    
    # 초기값 선언
    answer = 1
    limit = targets[0][1]
    
    for s,e in targets:
        if s < limit: # 같이 격추 가능
            limit = min(e, limit) # 포함된 경우 고려
        else:
            answer += 1 # 새로운 미사일을 사용해야함
            limit = e # 경계 최신화
            
    # 출력부
    return answer