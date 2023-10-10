# 빠른 입출력 및 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 초기 변수 선언
ladder = {}
snake = {}
queue = deque()
visited = [False for _ in range(101)]

# 입력부
N, M = map(int, input().split())
for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

# BFS 시작
queue.append((1,0))
while queue:
    # 값 뽑아오기
    pos, dice = queue.popleft()

    # 100번째 칸 도착
    if pos == 100:
        print(dice)
        break

    # 탐색이 불가한 경우
    # 1. 100번째 칸을 넘어버림
    if pos > 100: continue
    # 2. 이미 와본 적 있는 칸임
    if visited[pos]: continue

    # 탐색
    visited[pos] = True
    # 도착한 칸이 사다리이거나 뱀임 -> 이동 후 탐색 한번 더
    if pos in ladder.keys():
        pos = ladder[pos]
        visited[pos] = True
    if pos in snake.keys():
        pos = snake[pos]
        visited[pos] = True

    # 다음 탐색
    for i in range(1,7):
        queue.append((pos+i, dice+1))