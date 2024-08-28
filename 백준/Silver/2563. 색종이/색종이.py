# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 큰 색종이 선언
paper = [[False for _ in range(100)] for _ in range(100)]

# 입력부
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())

    # 색종이 붙이기
    for i in range(10):
        for j in range(10):
            paper[X+i][Y+j] = True

# 결과 도출 및 출력부
result = 0
for x in range(100):
    for y in range(100):
        if paper[x][y]: result += 1
print(result)