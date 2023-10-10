from collections import deque
n = int(input())
inputdeque = deque([int(input()) for _ in range(n)])

material = deque([i+1 for i in range(n)])
empty = deque()
made = deque()
result = deque()

while inputdeque != made:
    for i in range(n):
        while True:
            # print(empty, inputdeque[i], made)
            if empty and empty[-1] == inputdeque[i]:
                break
            if not material:
                print('NO')
                exit()
            empty.append(material.popleft())
            result.append('+')
            

        made.append(empty.pop())
        result.append('-')

print('\n'.join(result))