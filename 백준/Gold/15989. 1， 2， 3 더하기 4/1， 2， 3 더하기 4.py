# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for _ in range(T):
    n = int(input())

    # 초기값 선언
    DP = [0 for _ in range(n+1)]
    DP[0] = 1

    # Bottom-Up
    for number in range(1, 4): # 1부터 3까지 숫자 사용
        # (처음엔 1만 이용해서 기록 -> 이후 2 추가 -> 이후 3 추가)
        for idx in range(number, n+1): DP[idx] += DP[idx-number]

    # 출력부
    print(DP[n])