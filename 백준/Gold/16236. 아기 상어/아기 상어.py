# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(N)] for _ in range(N)]
result = 0
count = 0
size = 2

# heap 설정
for i in range(N):
    for j in range(N):
        if Map[i][j] == 9:
            Map[i][j] = 0
            heap = [(0, i, j)]

# 우선순위 큐 BFS
while heap:
    time, X, Y= heapq.heappop(heap)

    # 탐색 불가 조건
    # 1. 탐색하려는 위치는 범위를 벗어남
    if X < 0 or X >= N or Y < 0 or Y >= N: continue
    # 2. 탐색하려는 위치에 자신보다 큰 물고기가 있음
    if Map[X][Y] > size: continue
    # 3. 탐색하려는 위치는 물고기를 먹으러 가기전 이미 방문한 위치임
    if visited[X][Y]: continue

    # 탐색
    if Map[X][Y] and Map[X][Y] < size: # 잡아먹음
        count += 1
        if count == size: # 사이즈가 커짐
            size += 1
            count = 0
        Map[X][Y] = 0
        heap = [(time, X, Y)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        result = time

    visited[X][Y] = True

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        heapq.heappush(heap, (time+1, X_, Y_))

# 출력부
print(result)