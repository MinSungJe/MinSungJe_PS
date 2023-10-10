num = int(input())
results = []
for i in range(1,num+1):
    sum = 0
    sum += i // 1000000
    sum += (i%1000000) // 100000
    sum += (i%100000) // 10000
    sum += (i%10000) // 1000
    sum += (i%1000) // 100
    sum += (i%100) // 10
    sum += i % 10
    sum += i

    if sum == num:
        results.append(i)

print(results[0] if results else 0)