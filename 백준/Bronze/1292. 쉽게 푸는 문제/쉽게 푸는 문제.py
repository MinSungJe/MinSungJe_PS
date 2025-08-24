numbers = list()

idx = 1
while len(numbers) < 1001:
    for _ in range(idx): numbers.append(idx)
    idx += 1

A, B = map(int, input().split())
answer = sum(numbers[A-1:B])
print(answer)