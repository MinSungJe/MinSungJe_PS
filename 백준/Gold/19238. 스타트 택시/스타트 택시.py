# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, Gas = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())
pos = [X-1, Y-1]
target = list()
for i in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    Map[X1-1][Y1-1] = 2+i
    target.append((X1-1, Y1-1, X2-1, Y2-1))

# 전역변수 선언
INF = 401
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 태워야하는 손님 찾는 함수
def findPerson(x, y):
    # 초기값 선언
    rX, rY = INF, INF
    idx = INF
    distance = INF
    queue = deque([(x, y, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 모든 최단거리 내 값 확인 완료
        if count > distance: break

        # 도착
        if Map[X][Y] >= 2:
            distance = count
            if X < rX or (X == rX and Y < rY):
                idx = Map[X][Y] - 2
                rX, rY = X, Y


        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
            if Map[X_][Y_] == 1: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True

            # 다음 탐색
            queue.append((X_, Y_, count+1))
    
    if distance != INF: Map[rX][rY] = 0
    return idx, distance
    
# 해당 idx의 도착점까지의 최단거리 구하는 함수
def findArrival(x, y, idx):
    # 초기값 선언
    distance = INF
    queue = deque([(x, y, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    tX, tY = target[idx][2], target[idx][3]

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 도착
        if X == tX and Y == tY:
            distance = count
            break

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
            if Map[X_][Y_] == 1: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            
            # 다음 탐색
            queue.append((X_, Y_, count+1))

    return distance

# 함수 호출
for _ in range(M):
    # 가장 가까운 손님 찾아서 태우기
    idx, distance = findPerson(pos[0], pos[1])
    if distance >= INF or Gas < distance:
        Gas = -1
        break
    Gas -= distance
    pos[0], pos[1] = target[idx][0], target[idx][1]

    # 손님의 목적지까지 태우기
    distance = findArrival(pos[0], pos[1], idx)
    if distance >= INF or Gas < distance:
        Gas = -1
        break
    Gas += distance
    pos[0], pos[1] = target[idx][2], target[idx][3]

# 출력부
print(Gas)