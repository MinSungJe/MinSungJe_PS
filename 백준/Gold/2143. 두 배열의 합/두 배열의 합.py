# 모듈 불러오기
import bisect

# 입력부
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 누적합 배열 구학
SumA = [0 for _ in range(n+1)]
Sum = 0
for i in range(1,n+1):
    Sum += A[i-1]
    SumA[i] = Sum

SumB = [0 for _ in range(m+1)]
Sum = 0
for i in range(1,m+1):
    Sum += B[i-1]
    SumB[i] = Sum

# 부배열 합 구하기
subA = list()
for i in range(0, n):
    for j in range(i+1, n+1): subA.append(SumA[j] - SumA[i])
subB = list()
for i in range(0, m):
    for j in range(i+1, m+1): subB.append(SumB[j] - SumB[i])

# 한쪽 정렬
subB.sort()

# 이분 탐색
result = 0
for a in subA:
    target = T - a
    result += bisect.bisect_right(subB, target) - bisect.bisect_left(subB, target)

# 출력부
print(result)