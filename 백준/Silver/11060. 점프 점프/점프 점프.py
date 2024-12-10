# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
A = list(map(int, input().split()))

# 초기값 선언
result = -1
queue = deque([(0, 0)])
visited = [False for _ in range(N)]
visited[0] = True

# BFS
while queue:
    pos, count = queue.popleft()

    # 도착
    if pos == N-1:
        result = count
        break

    # 다음 탐색
    for i in range(A[pos]+1):
        pos_ = pos+i

        # 탐색 불가 조건
        if pos_ >= N: continue
        if visited[pos_]: continue

        # 탐색
        visited[pos_] = True

        # 다음 탐색
        queue.append((pos_, count+1))

# 출력부
print(result)