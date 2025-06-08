# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

while True:
    # 입력부
    N = int(input())
    if N == 0: break # 종료
    numbers = [int(input()) for _ in range(N)]

    # DP 배열 선언
    INF = 10001
    DP = [-INF for _ in range(N)]
    DP[0] = numbers[0]

    # DP 배열 채우기
    for i in range(1, N): DP[i] = max(DP[i-1]+numbers[i], numbers[i])

    # 출력부
    answer = max(DP)
    print(answer)