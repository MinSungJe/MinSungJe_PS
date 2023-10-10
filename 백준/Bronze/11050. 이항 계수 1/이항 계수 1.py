N, K = map(int, input().split())
numlist = [0] * 11

def factorial(num):
    if num == 0:
        numlist[num] = 1
        return numlist[num]
    
    if num == 1:
        numlist[num] = 1
        return numlist[num]
    
    if numlist[num] != 0:
        return numlist[num]
    
    numlist[num] = num * factorial(num-1)
    return numlist[num]

print(int(factorial(N)/(factorial(K)*factorial(N-K))))