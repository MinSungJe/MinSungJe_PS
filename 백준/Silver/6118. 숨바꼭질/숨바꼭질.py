# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 초기값 선언
queue = deque([(1, 0)])
distance = [-1 for _ in range(N+1)]

# BFS
while queue:
    node, count = queue.popleft()
    
    # 탐색 불가 조건
    if distance[node] != -1: continue

    # 탐색
    distance[node] = count

    # 다음 탐색
    for node_ in graph[node]: queue.append((node_, count+1))

# 결과값 구하기
answer = -1
answer_distance = -1
answer_count = 0
for i in range(1, N+1):
    if distance[i] == answer_distance: answer_count += 1
    if distance[i] > answer_distance:
        answer_distance = distance[i]
        answer = i
        answer_count = 1

# 출력부
print(answer, answer_distance, answer_count)