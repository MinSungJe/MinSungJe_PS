def solution(picks, minerals):
    answer = 0
    # 캘 수 있는 자원까지만 확인
    minerals = minerals[:sum(picks) * 5]
    
    # 가치 배열로 환산
    values = []
    for i, mineral in enumerate(minerals):
        if i % 5 == 0:
            if i != 0: values.append(temp)
            temp = [0,0,0]
        if mineral == 'diamond':
            temp[0] += 1
            temp[1] += 5
            temp[2] += 25
        if mineral == 'iron':
            temp[0] += 1
            temp[1] += 1
            temp[2] += 5
        if mineral == 'stone':
            temp[0] += 1
            temp[1] += 1
            temp[2] += 1
    values.append(temp)
    
    # 가치배열을 가치 순으로 정렬
    values.sort(key=lambda x:-x[2])
    
    # 피로도 계산
    for value in values:
        if picks[0] != 0:
            answer += value[0]
            picks[0] -= 1
        elif picks[1] != 0:
            answer += value[1]
            picks[1] -= 1
        else:
            answer += value[2]
            picks[2] -= 1
            
    return answer