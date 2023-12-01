# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
canPlace = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
result = [0, 0]
visited = [[0 for _ in range(N)] for _ in range(N)]


# DFS 함수 선언
def DFS(idx, count):
    # 탐색
    result[idx%2] = max(result[idx%2], count)
    
    # 범위를 벗어남
    if idx >= 2*N - 1: return

    # 해당 대각선의 칸들 탐색
    for i in range(N-abs(N-(idx+1))):
        X = min(idx, N-1) - i
        Y = max(idx-(N-1), 0) + i

        # 탐색 불가 조건
        if visited[X][Y]: continue
        
        # 탐색
        if canPlace[X][Y]: # 실제로 둔 경우
            for m in range(N):
                X_ = X + m
                Y_ = Y + m
                if X_ >= N or Y_ >= N: break
                visited[X_][Y_] += 1

            # 다음 탐색
            DFS(idx+2, count+1)

            # backtracking
            for m in range(N):
                X_ = X + m
                Y_ = Y + m
                if X_ >= N or Y_ >= N: break
                visited[X_][Y_] -= 1
        else: # 실제로 두지 않은 경우
            DFS(idx+2, count)

# 함수 선언
DFS(0, 0)
DFS(1, 0)

# 출력부
print(sum(result))