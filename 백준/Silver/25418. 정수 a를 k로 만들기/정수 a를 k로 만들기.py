# 모듈 불러오기
from collections import deque

# 입력부
A, K = map(int, input().split())

# 초기값 선언
result = 0
visited = [False for _ in range(1000001)]
queue = deque([(A, 0)])

# BFS
while queue:
    node, count = queue.popleft()
    
    # 탐색 불가 조건
    if node > K: continue
    if visited[node]: continue

    # 탐색
    if node == K: # 탐색 완료
        result = count
        break
    visited[node] = True

    # 다음 탐색
    for node_ in (node+1, node*2):
        queue.append((node_, count+1))

# 출력부
print(result)