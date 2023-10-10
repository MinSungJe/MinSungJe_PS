M,N = map(int,input().split())
result = []
for i in range(M,N+1):
    sosu = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            sosu = False
            break
    if sosu == True and i != 1:
        print(i)