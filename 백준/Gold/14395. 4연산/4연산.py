# 모듈 불러오기
from collections import deque

# 입력부
s, t = map(int, input().split())

# 초기값 선언
result = -1
operator = ['*', '+']
queue = deque([(s*s, '*'), (s+s, '+'), (0, '-'), (1, '/')])

# BFS
while queue:
    node, cmd = queue.popleft()

    # 탐색 불가 조건
    if node > t: continue

    # 탐색
    if node == t:
        result = cmd
        break

    # 다음 탐색
    for i in range(2):
        if i == 0: node_ = (node*node)
        if i == 1: node_ = (node+node)
        if node == node_: continue
        queue.append((node_, cmd+operator[i]))

# 출력부
print(result if s != t else 0)