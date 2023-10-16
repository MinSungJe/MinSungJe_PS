from collections import deque

def solution(maps):
    # 초기값 설정
    answer = -1
    N = len(maps)
    M = len(maps[0])
    queueL = deque()
    queueE = deque()
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)
    
    # 시작지점 찾아서 queue에 넣기
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S': queueL.append((i,j,0))
    
    # 레버 BFS 시작
    while queueL:
        X, Y, count = queueL.popleft()
        
        # 탐색 불가 조건
        # 1. 해당 지역은 범위를 벗어남
        if X < 0 or X >= N or Y < 0 or Y >= M: continue
        # 2. 해당 지역은 벽임
        if maps[X][Y] == 'X': continue
        # 3. 해당 지역은 이미 방문한 적 있음
        if visited[X][Y][0]: continue
        
        # 탐색 완료
        if maps[X][Y] == 'L':
            queueE.append((X,Y,count))
            break
        
        # 탐색
        visited[X][Y][0] = True
        
        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queueL.append((X_, Y_, count+1))
            
    # 탈출 BFS 시작
    while queueE:
        X, Y, count = queueE.popleft()
        
        # 탐색 불가 조건
        # 1. 해당 지역은 범위를 벗어남
        if X < 0 or X >= N or Y < 0 or Y >= M: continue
        # 2. 해당 지역은 벽임
        if maps[X][Y] == 'X': continue
        # 3. 해당 지역은 이미 방문한 적 있음
        if visited[X][Y][1]: continue
        
        # 탐색 완료
        if maps[X][Y] == 'E':
            answer = count
            break
        
        # 탐색
        visited[X][Y][1] = True
        
        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queueE.append((X_, Y_, count+1))
    
    
    return answer