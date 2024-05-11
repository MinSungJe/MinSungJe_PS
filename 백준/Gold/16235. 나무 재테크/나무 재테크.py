# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부(1)
N, M, K = map(int, input().split())
robot = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
energy = [[5 for _ in range(N)] for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
liveTree = [[deque() for _ in range(N)] for _ in range(N)]
deathTree = [[deque() for _ in range(N)] for _ in range(N)]

# 입력부(2)
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

# 봄
def spring():
    for i in range(N):
        for j in range(N):
            while tree[i][j]:
                value = tree[i][j].popleft()
                if energy[i][j] >= value:
                    liveTree[i][j].append(value+1)
                    energy[i][j] -= value
                else: deathTree[i][j].append(value)

            while liveTree[i][j]:
                value = liveTree[i][j].popleft()
                tree[i][j].append(value)

# 여름
def summer():
    for i in range(N):
        for j in range(N):
            while deathTree[i][j]:
                value = deathTree[i][j].popleft()
                energy[i][j] += (value//2)

# 가을
def fall():
    for X in range(N):
        for Y in range(N):
            for age in tree[X][Y]:
                if age % 5: continue
                for i in range(8):
                    X_, Y_ = X+dx[i], Y+dy[i]
                    if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
                    tree[X_][Y_].appendleft(1)

# 겨울
def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += robot[i][j]

# 함수 호출
for _ in range(K):
    spring()
    summer()
    fall()
    winter()

# 결과값 계산 및 출력부
result = 0
for i in range(N):
    for j in range(N): result += len(tree[i][j])
print(result)