N,K = map(int,input().split())
result = []
survivor = [i for i in range(1,N+1)]
target = 0

for i in range(N):
    target += K-1
    while target >= len(survivor):
        target -= len(survivor)
    result.append(survivor.pop(target))

print("<",end='')
print(", ".join(map(str,result)), end='')
print(">")