num = int(input())
numlist = []

for i in range(num):
    x, y = map(int,input().split())
    numlist.append([x,y])   
    
numlist.sort(key=lambda a:(a[0], a[1]))

for i in range(num):
    print(*numlist[i])