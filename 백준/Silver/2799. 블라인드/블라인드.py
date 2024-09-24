# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N = map(int, input().split())
window = [list(input()) for _ in range(5*M+1)]

# 창문 검사
result = [0, 0, 0, 0, 0]
for x in range(M):
    for y in range(N):
        startX, startY = 5*x+1, 5*y+1
        for i in range(4):
            if window[startX+i][startY] == '.':
                result[i] += 1
                break
        if window[startX+3][startY] == '*': result[4] += 1

# 출력부
print(*result)