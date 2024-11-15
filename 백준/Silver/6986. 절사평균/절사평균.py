# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())
numbers = list(float(input()) for _ in range(N))

# 정렬
numbers.sort()

# 절사총합과 보정총합 구하기
julsaTotal = sum(numbers[K:N-K])
bojungTotal = julsaTotal + (numbers[K] * K) + (numbers[N-K-1] * K)

# 절사 평균, 보정 평균 구하기
julsaResult = julsaTotal / (N-2*K) +1e-8
bojungResult = bojungTotal / N +1e-8

# 출력부
for result in (julsaResult, bojungResult):
    print(f"{result:.2f}")