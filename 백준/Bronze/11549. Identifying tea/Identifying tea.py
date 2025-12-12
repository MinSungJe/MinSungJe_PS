N = int(input())
teas = list(map(int, input().split()))

answer = 0
for tea in teas:
    if N == tea: answer += 1
        
print(answer)