# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
visited = [False for _ in range(ord('Z')+1)] # 유니코드 활용 문자를 숫자로 변환
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def DFS(X, Y, count):
    global result, visited

    # 결과값 최신화
    result = max(result, count)

    # 4방향 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]

        # 탐색 불가 조건
        # 1. 탐색하려는 구역이 범위를 넘어섬
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        # 2. 탐색하려는 구역의 알파벳은 이미 거침
        if visited[ord(Map[X_][Y_])]: continue

        # 탐색
        visited[ord(Map[X_][Y_])] = True

        # 다음 탐색
        DFS(X_,Y_,count+1)

        # backtracking
        visited[ord(Map[X_][Y_])] = False


# DFS 실행
visited[ord(Map[0][0])] = True
DFS(0,0,1)

# 출력부
print(result)