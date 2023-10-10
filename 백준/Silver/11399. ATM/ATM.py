# 입력부
N = int(input())
P = list(map(int, input().split()))

# 초기값 선언
sumP = [0 for _ in range(N)]
Sum = 0

# 정렬
P.sort()
for i in range(N):
    Sum += P[i]
    sumP[i] = Sum

# 출력부
print(sum(sumP))