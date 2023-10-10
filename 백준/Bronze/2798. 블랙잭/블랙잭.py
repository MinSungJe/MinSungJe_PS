N, M = map(int, input().split())
numlist = list(map(int,input().split()))
result = []

for i in range(N):
    for j in range(N):
        if j <= i:
            continue
        for k in range(N):
            if k <= j:
                continue
            sum = numlist[i] + numlist[j] + numlist[k]
            if sum > M:
                continue
            result.append(sum)

print(max(result))