# 입력부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 누적합
sum_numbers = [0 for _ in range(N+1)]
sum_numbers[1] = numbers[0]
for i in range(2, N+1): sum_numbers[i] = sum_numbers[i-1] + numbers[i-1]

# 수열의 합 비교
answer = 0
for i in range(N+1):
    for j in range(i+1, N+1):
        if sum_numbers[j] - sum_numbers[i] == M: answer += 1

# 출력부
print(answer)