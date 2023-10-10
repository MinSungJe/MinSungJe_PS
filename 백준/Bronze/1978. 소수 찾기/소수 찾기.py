num = int(input())

numlist = list(map(int,input().split()))
result = 0

for nums in numlist:
    sosu = True
    for i in range(1,nums+1):
        if nums == 1:
            sosu = False
            break
        if i == nums or i == 1:
            continue
        else:
            if nums % i == 0 :
                sosu = False
                break
    if sosu:
        result += 1

print(result)