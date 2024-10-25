# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]
N = int(input())
turn = list(map(int, input().split()))

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 클러스터링 함수
def clustering(x, y, idx):
    # 초기값 선언
    queue = deque([(x, y)])
    cluster[x][y] = idx

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
            if Map[X_][Y_] == '.': continue
            if cluster[X_][Y_]: continue

            # 탐색
            cluster[X_][Y_] = idx

            # 다음 탐색
            queue.append((X_, Y_))

# 얼마나 내릴지 확인
def check_fall(queue):
    result = 0
    while queue:
        X, Y, count = queue.popleft()
        X_ = X+1

        # 탐색 불가 조건
        if X_ >= R or Map[X_][Y] == 'x':
            result = count
            break
        
        # 다음 탐색
        queue.append((X_, Y, count+1))
    
    return result

# 싸움 시작
for idx in range(N):
    height = R-turn[idx]
    min_range, max_range, direction = 0, C, 1
    if (idx % 2): min_range, max_range, direction = C-1, -1, -1

    # 창 던지기
    for i in range(min_range, max_range, direction):
        if Map[height][i] == 'x':
            Map[height][i] = '.'
            break

    # 클러스터링
    cluster_idx = 1
    cluster = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if Map[x][y] == 'x' and not cluster[x][y]:
                clustering(x, y, cluster_idx)
                cluster_idx += 1

    # 행마다 탐색
    mineral = [deque() for _ in range(cluster_idx)]
    bottom = [deque() for _ in range(cluster_idx)]
    for column in range(C):
        cluster_visited = [False for _ in range(cluster_idx)]
        cluster_visited[0] = True
        for x in range(R-1, -1, -1):
            check_cluster = cluster[x][column]
            if check_cluster: mineral[check_cluster].append((x, column))
            if not cluster_visited[check_cluster]:
                bottom[check_cluster].append((x, column, 0))
                cluster_visited[check_cluster] = True
    
    # 클러스터별로 내릴 정도 확인
    for cluster in range(1, cluster_idx):
        value = check_fall(bottom[cluster])
        # 옮기기
        if not value: continue
        while mineral[cluster]:
            X, Y = mineral[cluster].popleft()
            Map[X][Y] = '.'
            Map[X+value][Y] = 'x'
    
# 출력부
for i in range(R): print(''.join(Map[i]))