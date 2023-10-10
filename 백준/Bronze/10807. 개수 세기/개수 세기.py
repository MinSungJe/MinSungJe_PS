num = int(input())
numlist = list(map(int,input().split()))
target = int(input())

result = 0
for i in numlist:
    if i == target:
        result += 1
        
print(result)