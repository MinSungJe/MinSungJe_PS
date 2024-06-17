# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
menu = list(map(int, input().split()))

# 초기값 선언
INF = 1000000007

# 분할정복 거듭제곱 구현
def Pow(a, b):
    if b == 0: return 1
    if b == 1: return a
    half = Pow(a, b//2)
    if b % 2: return (half * half * a) % INF
    else: return (half * half) % INF

# 메뉴 정렬
menu.sort()

# O(N) 탐색
result = 0
for i in range(N):
    # 선택된 원소가 최댓값인 조합 - 선택된 원소가 최솟값인 조합
    result += (menu[i] * (Pow(2, i) - Pow(2, N-i-1))) % INF

# 출력부
print(result % INF)