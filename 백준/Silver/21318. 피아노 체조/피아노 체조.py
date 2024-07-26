# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
piano = list(map(int, input().split()))

# 실수하는 구간의 누적합 구하기
miss = 0
Sum = [0 for _ in range(N)]
for i in range(N-1):
    Sum[i] = miss
    if piano[i] > piano[i+1]: miss += 1
Sum[N-1] = miss

# TC
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    
    # 결과 도출 및 출력부
    result = Sum[y-1] - Sum[x-1]
    print(result)