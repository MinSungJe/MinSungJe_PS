# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import permutations
import sys
def input(): return sys.stdin.readline().rstrip()

# 재귀 제한 해제
sys.setrecursionlimit(10**6)

# 입력부
plate = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]


# 초기값 선언
INF = 126
dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

# 탐색 함수
def BFS():
    # 초기값 선언
    result = INF
    if not cube[0][0][0] or not cube[4][4][4]: return result # 출발지, 도착지가 갈 수 없는 구역임
    visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True
    queue = deque([(0, 0, 0, 0)])

    # BFS
    while queue:
        X, Y, Z, count = queue.popleft()

        # 도착
        if X == 4 and Y == 4 and Z == 4:
            result = count
            break

        # 다음 탐색
        for i in range(6):
            X_, Y_, Z_ = X+dx[i], Y+dy[i], Z+dz[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= 5 or Y_ < 0 or Y_ >= 5 or Z_ < 0 or Z_ >= 5: continue
            if not cube[X_][Y_][Z_]: continue
            if visited[X_][Y_][Z_]: continue

            # 탐색
            visited[X_][Y_][Z_] = True

            queue.append((X_, Y_, Z_, count+1))

    if result == 12:
        print(result)
        exit()
    return result

# 돌리기
def rotate(idx):
    temp = [arr[:] for arr in cube[idx]]

    for i in range(5):
        for j in range(5): cube[idx][i][j] = temp[j][4-i]

def DFS(idx):
    # 탐색 시작
    if idx == 5: return BFS()
    
    # 모든 돌리는 경우를 확인
    result = min(INF, DFS(idx+1))
    for _ in range(3):
        rotate(idx)
        result = min(result, DFS(idx+1))

    return result

# 함수 호출 및 출력부
answer = INF
for sorted_plate in permutations(plate):
    cube = list(sorted_plate)
    answer = min(answer, DFS(0))
print(answer if answer < INF else -1)