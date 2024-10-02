# 모듈 불러오기
from collections import deque

# 입력부
a, b, c, d = map(int, input().split())

# 초기값 선언
queue = deque([(0, 0, 0)])
visited = dict()

# BFS
result = -1
while queue:
    A, B, count = queue.popleft()

    # 탐색 불가 조건
    if visited.get((A, B)): continue

    # 탐색
    visited[(A, B)] = True

    # 물을 목표대로 채움
    if A == c and B == d:
        result = count
        break

    # 다음 탐색
    queue.append((a, B, count+1)) # A에 물채움
    queue.append((A, b, count+1)) # B에 물채움
    queue.append((0, B, count+1)) # A 물을 비움
    queue.append((A, 0, count+1)) # B 물을 비움
    bSpace = b-B
    Awater = min(A, bSpace)
    queue.append((A-Awater, B+Awater, count+1)) # A의 물을 B에 채움
    aSpace = a-A
    bwater = min(B, aSpace)
    queue.append((A+bwater, B-bwater, count+1)) # B의 물을 A에 채움

# 출력부
print(result)