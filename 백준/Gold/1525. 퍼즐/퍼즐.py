# 모듈 불러오기
from collections import deque

# 입력부
startMap = [list(input().split()) for _ in range(3)]

# 맵을 코드로 변환하는 함수
def map2Code(Map):
    result = ''
    for i in range(3):
        for j in range(3):
            result += str(Map[i][j])

    return result

# 코드를 맵으로 변환하는 함수
def code2Map(code):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            result[i][j] = code[(3*i)+j]

    return result

# 초기값 선언
result = -1
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
startCode = map2Code(startMap)
visited = set([startCode])
queue = deque([(startCode, 0)])

# BFS
while queue:
    mapCode, count = queue.popleft()
    Map = code2Map(mapCode)
    
    # 정렬 완료
    if mapCode == '123456780':
        result = count
        break

    # 0인부분 찾기
    for x in range(3):
        for y in range(3):
            if Map[x][y] == '0': X, Y = x, y

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 교환 불가 조건
        if X_ < 0 or X_ >= 3 or Y_ < 0 or Y_ >= 3: continue
        
        # 교환
        temp = [arr[:] for arr in Map]
        temp[X][Y] = temp[X_][Y_]
        temp[X_][Y_] = '0'

        # 중복 확인
        tempCode = map2Code(temp)
        if visited.intersection({tempCode}): continue

        # 탐색
        visited.add(tempCode)

        # 다음 탐색
        queue.append((tempCode, count+1))

# 출력부
print(result)