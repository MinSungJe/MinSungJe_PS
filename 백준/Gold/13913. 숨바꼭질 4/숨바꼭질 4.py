# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())

# 초기값 선언
result = 0
way = list()
visited = [-1 for _ in range(100001)]
queue = deque([(N, 0)])

# BFS
while queue:
    node, count = queue.popleft()
    
    # 도착
    if node == K:
        result = count # 횟수 기록

        # 거쳐온 길 구하기
        idx = K
        while True:
            if idx == N:
                way.append(idx)
                break # 종료
            way.append(idx)
            idx = visited[idx]
        break

    # 탐색
    for node_ in (node-1, node+1, 2*node):

        # 탐색 불가 조건
        if node_ < 0 or node_ > 100000: continue
        if visited[node_] != -1: continue
        
        # 기록
        visited[node_] = node

        queue.append((node_, count+1))

# 출력부 
print(result)
print(*way[::-1])