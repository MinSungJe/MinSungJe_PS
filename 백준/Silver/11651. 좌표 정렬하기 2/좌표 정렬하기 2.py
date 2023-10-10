num = int(input())
dots = []
for i in range(num):
    x,y = map(int,input().split())
    dots.append([x,y])

dots.sort(key=lambda a:(a[1],a[0]))
for i in range(num):
    print(*dots[i])