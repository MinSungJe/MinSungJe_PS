# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for test_case in range(1, T+1):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]

    # 초기값 선언
    fast_result = 0
    late_result = 0

    # 최솟값, 최댓값 구하기
    for ant in ants:
        fast_result = max(fast_result, min(l-ant, ant))
        late_result = max(late_result, max(l-ant, ant))
    
    # 출력부
    print(fast_result, late_result)