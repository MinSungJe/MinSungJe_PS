import sys
num = int(sys.stdin.readline())
numlist = [0] * 10001
for i in range(num):
    numlist[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numlist[i] != 0:
        for j in range(numlist[i]):
            print(i)