# 입력부
N, K = map(int, input().split())
numberList = list(map(int, input().split()))

# 누적합 리스트 구하기
sumList = [0 for _ in range(N)]
sumList[0] = numberList[0]
for i in range(1, N):
    sumList[i] = sumList[i-1]+numberList[i]
sumList = [0] + sumList

# 최댓값 구하기
result = -10000001
for i in range(K, N+1):
    value = sumList[i] - sumList[i-K]
    result = max(result, value)

# 출력부
print(result)