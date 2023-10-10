# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
result = 0
# 블럭 선언 :
# 세로 일자블럭, 네모블럭, ㄹ가로1, ㄹ가로2, ㅗ, ㅜ, L가로1, L가로2, L가로3, L가로4,
# ㄹ세로1, ㄹ세로2, ㅓ, ㅏ, L세로1, L세로2, L세로3, L세로4
dx = ((0,1,2,3),(0,1,0,1),(0,0,1,1),(0,0,1,1),(0,1,1,1),(0,0,0,1),(0,1,1,1),(0,1,1,1),(0,0,0,1),(0,0,0,1),
      (0,1,1,2),(0,1,1,2),(0,1,1,2),(0,1,1,2),(0,1,2,2),(0,1,2,2),(0,0,1,2),(0,0,1,2))
dy = ((0,0,0,0),(0,0,1,1),(0,1,1,2),(1,2,0,1),(1,0,1,2),(0,1,2,1),(0,0,1,2),(2,0,1,2),(0,1,2,2),(0,1,2,0),
      (0,0,1,1),(1,0,1,0),(1,0,1,1),(0,0,1,0),(0,0,0,1),(1,1,1,0),(0,1,0,0),(0,1,1,1))


# 가로 일자블럭
for i in range(N):
    row = Map[i]
    for j in range(M-3):
        Sum = sum(row[j:j+4])
        if Sum > result: result = Sum

# 세로 일자블럭
for i in range(N-3):
    for j in range(M):
        Sum = 0
        for k in range(4):
            Sum += Map[i+dx[0][k]][j+dy[0][k]]
        if Sum > result: result = Sum

# 네모 블럭
for i in range(N-1):
    for j in range(M-1):
        Sum = 0
        for k in range(4):
            Sum += Map[i+dx[1][k]][j+dy[1][k]]
        if Sum > result: result = Sum

# 2*3 크기 블럭들 시작, 총 8개
for i in range(N-1):
    for j in range(M-2):
        for block in range(2,10):
            Sum = 0
            for k in range(4):
                Sum += Map[i+dx[block][k]][j+dy[block][k]]
            if Sum > result: result = Sum

# 3*2 크기 블럭들 시작, 총 8개
for i in range(N-2):
    for j in range(M-1):
        for block in range(10,18):
            Sum = 0
            for k in range(4):
                Sum += Map[i+dx[block][k]][j+dy[block][k]]
            if Sum > result: result = Sum

# 결과 출력
print(result)