S1, S2, S3 = map(int, input().split())
numbers = [0 for _ in range(81)]

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1): numbers[i+j+k] += 1
max_value = max(numbers)

answer = 0
for i in range(1, 81):
    if numbers[i] == max_value:
        answer = i
        break
print(answer)