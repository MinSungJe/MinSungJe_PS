# 입력부
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 누적합 구하기
sumA = [0 for _ in range(N)]
sumA[0] = A[0]
for i in range(1, N): sumA[i] = sumA[i-1]+A[i]

# 누적합들의 나머지값 추합
rest = [0 for _ in range(M)]
for i in range(N): rest[sumA[i]%M] += 1

# nC2 구하는 함수
def C(n): return (n*(n-1)) // 2

# 결과값 도출 및 출력부
result = rest[0]
for i in range(M): result += C(rest[i])
print(result)