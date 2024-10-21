# 빠른 입력 및 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
INF = 1101

# DFS
def DFS(idx, visited):
    # 탐색 종료
    if idx == 11: return 0
    # 메모이제이션
    if DP[idx][visited] != -1: return DP[idx][visited]

    # 다음 탐색
    result = 0
    for position in range(11):
        # 탐색 불가 조건
        if power[idx][position] == 0: continue
        if visited & (1 << position): continue

        # 탐색
        visited_ = visited | (1 << position)

        # 다음 탐색
        result = max(result, power[idx][position]+DFS(idx+1, visited_))

    # 선수를 추가하지 못함
    if result == 0: return -INF

    # 메모이제이션
    DP[idx][visited] = result
    return result

# TC
T = int(input())
for test_case in range(1, T+1):
    power = [list(map(int, input().split())) for _ in range(11)]

    # 초기값 선언
    DP = [[-1 for _ in range(1<<11)] for _ in range(11)]

    # 함수 호출 및 출력부
    result = DFS(0, 0)
    print(result)