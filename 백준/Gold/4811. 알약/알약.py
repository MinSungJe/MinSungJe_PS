# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 약 먹는 함수(DFS+DP)
def medicine(W, H):
    # 탐색 종료
    if not W and H == 1: return 1
    # 메모이제이션
    if DP[W][H]: return DP[W][H]

    # 다음 탐색
    result = 0
    if not W: result += medicine(W, H-1)
    if not H: result += medicine(W-1, H+1)
    if W and H: result += medicine(W, H-1) + medicine(W-1, H+1)

    # 메모이제이션
    DP[W][H] = result

    return result

# TC
while True:
    # 입력부
    N = int(input())
    if not N: break

    # DP 배열 선언
    DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

    # 함수 호출 및 출력부
    result = medicine(N, 0)
    print(result)