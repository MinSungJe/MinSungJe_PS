# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for _ in range(T):
    N = int(input())

    # 초기값 선언
    dt = (-1, 1, -10, 10, 60)
    visited = [False for _ in range(61)]
    visited[0] = True
    queue = deque([(0, [N//60, 0, 0, 0, 0])])

    # BFS
    while queue:
        time, btns = queue.popleft()

        # 탐색 완료
        if time == N%60:
            result = btns[:]
            break

        # 다음 탐색
        for i in range(5):
            time_ = time + dt[i]
            btns_ = btns[:]
            btns_[4-i] += 1 

            # 탐색 불가 조건
            if time_ < 0 or time_ >= 61: continue
            if visited[time_]: continue

            # 탐색
            visited[time_] = True

            # 다음 탐색
            queue.append((time_, btns_))

    # 출력부
    print(*result)