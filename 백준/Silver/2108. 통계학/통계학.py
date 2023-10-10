import sys

num = int(sys.stdin.readline())
counts = [0] * 8001
sum = 0
idx = 0
many = 0
manys = 0

numlist = []
for i in range(num):
    numlist.append(int(sys.stdin.readline()))
    counts[numlist[i]+4000] += 1

for i in range(8001):
    if counts[i] != 0:
        for j in range(counts[i]):
            sum += (i-4000)
            if idx == (num//2):
                center = (i-4000)
            if idx == 0:
                low = (i-4000)
            if idx == num-1:
                high = (i-4000)
            
            idx += 1
        if counts[i] == max(counts):
                manys += 1
                if manys == 1:
                    many = (i-4000)
                if manys == 2:
                    many = (i-4000)
                

print(round(sum/num))
print(center)
print(many)
print(high-low)