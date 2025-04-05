# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())

    # 내선, 외선 구하기
    if a < b:
        inner = b-a
        outer = 43+a-b
    else:
        inner = 43+b-a
        outer = a-b
    
    # 출력부
    print('Same' if inner == outer else 'Inner circle line' if inner < outer else 'Outer circle line')