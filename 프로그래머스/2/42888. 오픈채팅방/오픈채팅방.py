def solution(record):
    answer = []
    id = {}
    
    # ID 변경사항 저장
    for r in record:
        cmd = list(r.split())
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            id[cmd[1]] = cmd[2]
            
    # 출력사항 저장
    for r in record:
        cmd = list(r.split())
        if cmd[0] == 'Enter':
            answer.append(f"{id[cmd[1]]}님이 들어왔습니다.")
        if cmd[0] == 'Leave':
            answer.append(f"{id[cmd[1]]}님이 나갔습니다.")
    
    
    return answer