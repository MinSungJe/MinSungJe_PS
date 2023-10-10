N = int(input())
cards = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))
dict = {}

for i in cards:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    
result = []

for i in nums:
    if i in dict:
        result.append(dict[i])
    else:
        result.append(0)

print(*result)