num = int(input())
result = []
for i in range(num):
    result.append(int(input()))
result.sort()

for i in range(num):
    print(result[i])