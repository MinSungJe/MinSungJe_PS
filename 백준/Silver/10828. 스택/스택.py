from collections import deque
import sys

num = int(sys.stdin.readline())
stack = deque()

for i in range(num):
    command = sys.stdin.readline()

    if command[0:4] == 'push':
        stack.append(int(command[5:]))

    if command[0:3] == 'pop':
        if stack != deque([]):
            print(stack.pop())
        else:
            print('-1')

    if command[0:3] == 'top':
        if stack != deque([]):
            print(stack[-1])
        else:
            print('-1')

    if command[0:5] == 'empty':
        if stack != deque([]):
            print('0')
        else:
            print('1')

    if command[0:4] == 'size':
        print(len(stack))    