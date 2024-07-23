# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for _ in range(T):
    # 입력부
    letter = input()

    # 초기값 선언
    N = int(len(letter) ** (1/2))
    result = ''

    # 암호 해독
    for x in range(N):
        for y in range(N):
            result += letter[N*y+(N-1-x)]

    # 출력부
    print(result)