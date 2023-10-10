from collections import deque
import sys
num = int(input())
numlist = deque()

for i in range(num):
    command = sys.stdin.readline()
    if command[0:10] == 'push_front':
        numlist.appendleft(int(command[11:]))
    
    if command[0:9] == 'push_back':
        numlist.append(int(command[10:]))
    
    if command[0:9] == 'pop_front':
        if numlist:
            print(numlist.popleft())
        else:
            print(-1)
    
    if command[0:8] == 'pop_back':
        if numlist:
            print(numlist.pop())
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