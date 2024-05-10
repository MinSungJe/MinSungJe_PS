# 모듈 불러오기
from collections import deque

# 입력부
Map = [list(input()) for _ in range(12)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


# 4개 뭉친 블럭을 터뜨리는 함수
def boom():
    # 초기값 선언
    visited = [[False for _ in range(6)] for _ in range(12)]
    boomBlock = deque()

    for i in range(12):
        for j in range(6):
            # 탐색 불가 조건
            if visited[i][j] or Map[i][j] == '.': continue
        
            # BFS
            count = 0
            queue = deque([(i, j, Map[i][j])])
            while queue:
                X, Y, color = queue.popleft()
                
                # 탐색 불가 조건
                if X < 0 or X >= 12 or Y < 0 or Y >= 6: continue
                if Map[X][Y] != color: continue
                if visited[X][Y]: continue

                # 탐색
                visited[X][Y] = True
                count += 1

                # 4방향 탐색
                for d in range(4):
                    X_, Y_ = X+dx[d], Y+dy[d]
                    queue.append((X_, Y_, color))
            
            if count >= 4: boomBlock.append((i, j, Map[i][j]))
        
    result = len(boomBlock) # 결과 저장

    # 터뜨리기
    while boomBlock:
        X, Y, color = boomBlock.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= 12 or Y < 0 or Y >= 6: continue
        if Map[X][Y] != color: continue

        # 탐색 및 터뜨리기
        Map[X][Y] = '.'

        # 다음 탐색
        for d in range(4):
            X_, Y_ = X+dx[d], Y+dy[d]
            boomBlock.append((X_, Y_, color))
    
    return result

# 빈 공간 내리는 함수
def down():
    for Y in range(6):
        temp = list()
        for X in range(11, -1, -1):
            value = Map[X][Y]
            if value != '.':
                temp.append(value)
                Map[X][Y] = '.'
        
        idx = 11
        for value in temp:
            Map[idx][Y] = value
            idx -= 1

# 함수 호출 및 결과값 도출
result = 0
while True:
    count = boom()
    if not count: break
    result += 1
    down()

# 출력부
print(result)