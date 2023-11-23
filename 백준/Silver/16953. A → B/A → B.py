# 모듈 불러오기
from collections import deque

# 입력부
A, B = map(int, input().split())

# 초기값 설정
result = -1

# queue 설정
queue = deque([(A, 1)])

# BFS
while queue:
    number, count = queue.popleft()

    # 탐색 불가 조건 : 탐색하려는 위치는 B를 벗어남
    if number > B: continue

    # 탐색
    if number == B:
        result = count
        break

    # 다음 탐색
    queue.append((number*2, count+1))
    queue.append(((10*number)+1, count+1))

# 출력부
print(result)