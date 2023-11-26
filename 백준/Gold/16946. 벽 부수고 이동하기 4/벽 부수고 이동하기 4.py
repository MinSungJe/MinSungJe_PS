# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(M)] for _ in range(N)]
result = [[0 for _ in range(M)] for _ in range(N)]
group = {}
group_label = 2

# BFS 함수 선언
def BFS(x, y, label):
    global visited, Map

    # 초기값 선언
    queue = deque([(x, y)])
    count = 1
    Map[x][y] = label
    visited[x][y] = True

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
            if Map[X_][Y_] == 1: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            Map[X_][Y_] = label
            count += 1

            # 다음 탐색
            queue.append((X_, Y_))
    
    return count
    

# 빈 공간을 분류하기
for i in range(N):
    for j in range(M):
        if not Map[i][j]:
            group[group_label] = BFS(i, j, group_label)
            group_label += 1

# 벽의 상하좌우 확인 후 분류된 빈 공간 더하기
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            used_group = []
            count = 1
            for k in range(4):
                i_ = i + dx[k]
                j_ = j + dy[k]

                # 탐색 불가 조건
                if i_ < 0 or i_ >= N or j_ < 0 or j_ >= M: continue
                if Map[i_][j_] == 1: continue
                if Map[i_][j_] in used_group: continue

                # 탐색
                used_group.append(Map[i_][j_])
                count += group[Map[i_][j_]] % 10
            
            # 결과값 저장
            result[i][j] = count % 10

# 출력부
for row in result:
    print(''.join(map(str, row)))