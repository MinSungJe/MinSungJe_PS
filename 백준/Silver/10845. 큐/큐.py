from collections import deque
import sys
num = int(input())
numlist = deque()

for i in range(num):
    command = sys.stdin.readline()
    if command[0:4] == 'push':
        numlist.append(int(command[5:]))
    
    if command[0:3] == 'pop':
        if numlist:
            print(numlist.popleft())
        else:
            print(-1)

    if command[0:4] == 'size':
        print(len(numlist))

    if command[0:5] == 'empty':
        if numlist:
            print(0)
        else:
            print(1)

    if command[0:5] == 'front':
        if numlist:
            print(numlist[0])
        else:
            print(-1)

    if command[0:4] == 'back':
        if numlist:
            print(numlist[-1])
        else:
            print(-1)