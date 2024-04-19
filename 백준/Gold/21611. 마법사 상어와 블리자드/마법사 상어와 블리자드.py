# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]
answer = [0, 0, 0, 0]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 순서 담는 리스트 제작
def getOrder():
    # 초기값 선언
    result = deque()
    pos = [N//2, N//2]
    Dx = (0, 1, 0, -1)
    Dy = (-1, 0, 1, 0)
    D = 0

    for i in range(1, N):
        for _ in range(2):
            for _ in range(i):
                pos[0] += Dx[D]
                pos[1] += Dy[D]
                result.append((pos[0], pos[1]))
            D = (D+1)%4
    
    for y in range(N-2, -1, -1): result.append((0, y))

    return result

order = getOrder()

# 현재 맵의 큐를 제작
def getQueue():
    result = deque()

    for x, y in order:
        value = Map[x][y]
        if value: result.append(value)

    return result

# 큐를 맵에 반영
def setMap(queue):
    global Map

    result = [[0 for _ in range(N)] for _ in range(N)]
    idx = 0
    while queue:
        if idx == (N*N)-1: break
        value = queue.popleft()
        X, Y = order[idx]
        result[X][Y] = value
        idx += 1
    Map = result

# 큐의 값들을 그룹으로 묶어주는 함수
def grouping(queue):
    marble = 0
    count = 0
    result = deque()
    while queue:
        value = queue.popleft()
        if value != marble:
            if marble: result.append((count, marble))
            count = 1
            marble = value
        else: count += 1
    if marble: result.append((count, marble))

    return result

# 폭발 단계
def explode():
    global answer

    temp = getQueue()
    # 터지지 않을때까지 반복
    bomb = True
    while bomb:
        # 초기값 선언
        bomb = False
        groupedQueue = grouping(temp)
        temp = deque()

        for count, marble in groupedQueue:
            if count >= 4: # 구슬 폭발
                bomb = True
                answer[marble] += count
                continue
            for _ in range(count): temp.append(marble)
    
    setMap(temp) # 맵에 반영

# 변화 단계
def change():
    # 초기값 선언
    temp = deque()
    groupedQueue = grouping(getQueue())

    for count, marble in groupedQueue:
        temp.append(count)
        temp.append(marble)

    setMap(temp) # 맵에 반영

# 마법 사용
for d, s in magic:
    # 블리자드 시전
    for m in range(1, s+1):
        X, Y = (N//2)+(dx[d-1]*m), (N//2)+(dy[d-1]*m)
        Map[X][Y] = 0

    # 폭발 단계
    explode()

    # 변화 단계
    change()

# 출력부
result = (1*answer[1])+(2*answer[2])+(3*answer[3])
print(result)