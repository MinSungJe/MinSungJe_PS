# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
while True:
    # 입력부
    N, M = map(int, input().split())
    if not N and not M: break
    NCD = [int(input()) for _ in range(N)]

    # 이분 탐색
    def BS(target):
        S = 0
        E = N
        result = False
        while S < E:
            M = (S + E) // 2

            if NCD[M] == target:
                result = True
                break

            if NCD[M] < target:
                S = M+1
            
            if NCD[M] > target:
                E = M

        return result

    # 함수 호출 및 결과값 도출
    result = 0
    for _ in range(M):
        number = int(input())
        if BS(number): result += 1

    # 출력부
    print(result)