# 모듈 불러오기
from collections import deque

# 입력부
N, k = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(2)]

# 초기값 선언
queue = deque([(0, 0, 0)])
visited = [[False for _ in range(N+1)] for _ in range(2)]

# BFS
result = False
while queue:
    pos, idx, count = queue.popleft()

    # 도착
    if idx >= N:
        result = True
        break

    # 탐색 불가 조건
    if idx < count: continue
    if Map[pos][idx] == 0: continue
    if visited[pos][idx]: continue

    # 탐색
    visited[pos][idx] = True

    # 다음 탐색
    for pos_, idx_  in [(pos, idx+1), (pos, idx-1), (1-pos, idx+k)]:
        queue.append((pos_, idx_, count+1))

# 출력부
print(1 if result else 0)