# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
# 입력부
A, B, C = map(int, input().split())

# 분할정복을 이용한 거듭제곱(O(logN))
def POW(a, b, c):
    # 분할 완료
    if b == 1:
        return a%c
    if b == 2:
        return (a*a) % c
    
    # 분할정복
    d = POW(a, b//2, c)
    if b % 2 == 0: # 지수가 짝수임
        return (d * d) % c
    else: # 지수가 홀수임
        return (d * d * a) % c

# 출력부
print(POW(A,B,C))