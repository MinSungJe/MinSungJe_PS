# 빠른 입력 및 모듈 불러오기
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 유클리드 호제법 이용 GCD 구하는 함수
def getGCD(A, B):
    while B > 0: A, B = B, A % B
    return A

# 입력부
N = int(input())
for _ in range(N):
    M = list(map(int, input().split()))

    # 모든 경우에 대해 탐색
    result = 0
    for A, B in combinations(M, 2):
        value = getGCD(A, B)
        result = max(result, value)
    
    # 출력부
    print(result)