# 모듈 불러오기
from collections import deque

# TC
C = int(input())
for test_case in range(1, C+1):
    # 입력부
    S, T = map(int, input().split())

    # 초기값 선언
    queue = deque([(S, T, 0)])
    visited = [[False for _ in range(201)] for _ in range(201)]

    # BFS
    while queue:
        s, t, count = queue.popleft()

        # 탐색 종료
        if s == t:
            answer = count
            break

        # 팀색 불가 조건
        if visited[s][t]: continue

        # 탐색
        visited[s][t] = True

        # 다음 탐색
        change_list = [(s+1, t), (2*s, t+3)]
        for s_, t_ in change_list:
            if s_ <= t_: queue.append((s_, t_, count+1))

    # 출력부
    print(answer)