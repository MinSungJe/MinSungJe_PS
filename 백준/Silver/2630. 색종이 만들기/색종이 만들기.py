# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

# 초기값 선언
white = 0
blue = 0

# 분할 정복 정의
def cut(X,Y,length):
    global white, blue

    # 분할성공
    Sum = 0
    for i in range(X,X+length):
        Sum += sum(paper[i][Y:Y+length])
    if Sum == 0: # 전부 0인 경우 -> 하얀색 색종이
        white += 1
        return
    if Sum == length * length: # 전부 1인 경우 -> 파란색 색종이
        blue += 1
        return
    
    # 분할
    for X_ in range(X,X+length,length//2):
        for Y_ in range(Y,Y+length,length//2):
            cut(X_,Y_,length//2)

# 분할정복 시작점 지정
cut(0,0,N)

# 출력부
print(white)
print(blue)