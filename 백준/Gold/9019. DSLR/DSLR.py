# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for test_case in range(1,T+1):
    A, B = map(int, input().split())

    # 초기값 선언
    queue = deque([(A,'')])
    visited = [False for _ in range(10000)]
    def D(N): return (2*N) % 10000
    def S(N): return N-1 if N != 0 else 9999
    def L(N): return (10 * (N % 1000)) + (N // 1000)
    def R(N): return (1000 * (N % 10)) + (N // 10)

    # BFS
    while queue:
        X, cmd = queue.popleft()

        # 탐색 성공
        if X == B:
            print(cmd)
            break

        # 다음 탐색 : D
        DX = D(X)
        # 탐색 가능 조건: 이미 방문한 적 없음
        if not visited[DX]:
            visited[DX] = True  # 방문처리
            queue.append((DX, cmd+'D'))

        # 다음 탐색 : S
        SX = S(X)
        # 탐색 가능 조건: 이미 방문한 적 없음
        if not visited[SX]:
            visited[SX] = True  # 방문처리
            queue.append((SX, cmd+'S'))
        
        # 다음 탐색 : L
        LX = L(X)
        # 탐색 가능 조건: 이미 방문한 적 없음
        if not visited[LX]:
            visited[LX] = True  # 방문처리
            queue.append((LX, cmd+'L'))
        
        # 다음 탐색 : R
        RX = R(X)
        # 탐색 가능 조건: 이미 방문한 적 없음
        if not visited[RX]:
            visited[RX] = True  # 방문처리
            queue.append((RX, cmd+'R'))