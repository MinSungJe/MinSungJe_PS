# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K, M = map(int, input().split())

# 그래프(역+하이퍼튜브) 선언
graph = [list() for _ in range(N+M+1)]

# 하이퍼튜브 입력받기
for i in range(M):
    hypertube = list(map(int, input().split()))
    for station in hypertube:
        tube_index = N+i+1
        graph[station].append(tube_index)
        graph[tube_index].append(station)

# 초기값 선언
result = -1
queue = deque([(1, 1)])
visited = [False for _ in range(N+M+1)]

# BFS
while queue:
    node, count = queue.popleft()

    # 탐색 불가 조건
    if visited[node]: continue

    # 탐색
    visited[node] = True
    if node == N:
        result = count
        break

    # 다음 탐색
    for node_ in graph[node]:
        if node_ > N: queue.append((node_, count)) # 역에서 하이퍼튜브로 이동
        else: queue.append((node_, count+1)) # 하이퍼튜브에서 역으로 이동

# 출력부
print(result)