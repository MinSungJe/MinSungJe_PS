# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 타입 변환 함수
def convertType(arr):
    return (int(arr[0]), int(float(arr[1])*100+0.5))

INF = 10001

while True:
    # 입력부
    n, m = convertType(input().split())
    if not n and not m: break
    
    # DP 배열 선언
    DP = [0 for _ in range(m+1)]

    # DP 배열 채우기(배낭)
    for i in range(1, n+1):
        c, p = convertType(input().split())
        for j in range(m+1):
            if j < p: continue
            else: DP[j] = max(DP[j], DP[j-p]+c)

    # 출력부
    print(DP[m])