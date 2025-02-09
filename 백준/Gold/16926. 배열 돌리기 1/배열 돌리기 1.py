# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열을 1차원 배열로 변환
rows = list()
for i in range(min(N, M) // 2):
    row = deque()
    row.extend(Map[i][i:M-1-i])
    row.extend([line[M-1-i] for line in Map[i:N-1-i]])
    row.extend(Map[N-1-i][M-1-i:i:-1])
    row.extend([line[i] for line in Map[N-1-i:i:-1]])
    rows.append(row)

# 모든 row 돌리기
for row in rows: row.rotate(-R)

# 2차원 배열로 변환
result = [[0 for _ in range(M)] for _ in range(N)]
for i in range(min(N, M) // 2):
    row = rows[i]
    for j in range(i, M-1-i): result[i][j] = row.popleft()
    for j in range(i, N-1-i): result[j][M-1-i] = row.popleft()
    for j in range(M-1-i, i, -1): result[N-1-i][j] = row.popleft()
    for j in range(N-1-i, i, -1): result[j][i] = row.popleft()

# 출력부
for row in result: print(*row)