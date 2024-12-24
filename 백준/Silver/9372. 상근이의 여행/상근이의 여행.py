# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, M = map(int, input().split())
    for _ in range(M):
        A, B = map(int, input().split())
    
    result = N-1
    
    # 출력부
    print(result)