# 모듈 불러오기
from collections import deque
# 입력부
N, K = map(int, input().split())

# 중복 방지를 위한 배열 선언
visited = [False for _ in range(100001)]

# BFS를 위한 queue 선언 및 초기값 넣기
queue = deque()
queue.append(N)
queue.append(0)

# BFS 구현
while queue:
    # queue에서 값 뽑기
    number = queue.popleft()
    time = queue.popleft()

    # 탐색을 하면 안되는 경우
    # 1. K가 될 수 있는 범위를 넘어섬
    if number < 0 or number > 100000: continue
    # 2. 이미 탐색한 숫자임
    if visited[number]: continue

    # K값을 찾음
    if number == K:
        print(time)
        break

    # 탐색
    visited[number] = True


    # 다음 탐색 : N+1, N-1, 2*N
    queue.append(number+1)
    queue.append(time+1)

    queue.append(number-1)
    queue.append(time+1)

    queue.append(2*number)
    queue.append(time+1)