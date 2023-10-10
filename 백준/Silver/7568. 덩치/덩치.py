T = int(input())
numlist = [list(map(int, input().split())) for i in range(T)]
result = []

for i in range(T):
    count = 0
    for j in range(T):
        if numlist[i][0] < numlist[j][0] and numlist[i][1] < numlist[j][1]:
            count += 1
    result.append(count + 1)

print(*result)