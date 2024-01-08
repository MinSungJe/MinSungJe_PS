# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# CCTV 정보 담기
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
dCCTV = [[],
         [(1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0)],
         [(1, 1, 0, 0), (0, 0, 1, 1)],
         [(1, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0)],
         [(1, 0, 1, 1), (1, 1, 0, 1), (0, 1, 1, 1), (1, 1, 1, 0)],
         [(1, 1, 1, 1)]]

# CCTV 위치 및 개수 확인
CCTV = list()
C = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] and Map[i][j] < 6:
            C += 1
            CCTV.append((Map[i][j], i, j))

# 사각지대 구하는 함수
def findZone(board):
    result = 0
    for i in range(N):
        for j in range(M):
            if not board[i][j]: result += 1
    
    return result

# DFS 완전탐색
def DFS(count, board):
    if count == C: return findZone(board) # 모든 CCTV 확인 완료

    targetC = CCTV[count]

    # 다음 탐색
    min_result = 65
    for d in dCCTV[targetC[0]]:
        temp = [arr[:] for arr in board] # backtracking
        for i in range(4):
            for m in range(1, 9):
                X_ = targetC[1] + (dx[i]*d[i]*m)
                Y_ = targetC[2] + (dy[i]*d[i]*m)

                if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: break
                if temp[X_][Y_] == 6: break

                if temp[X_][Y_] == 0: temp[X_][Y_] = -1
        
        min_result = min(min_result, DFS(count+1, temp))

    return min_result

# 함수 호출 및 출력부
result = DFS(0, Map)
print(result)