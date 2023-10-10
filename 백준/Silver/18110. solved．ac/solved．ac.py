import sys
from collections import deque

def makeround(i):
    num = i
    if num%1 >= 0.5:
        num = num - num%1 + 1
    else:
        num = num - num%1
    
    return int(num)

T = int(sys.stdin.readline())
people = makeround(T * 0.15)

scorelist = []

for test_case in range(1,T+1):
    scorelist.append(int(sys.stdin.readline()))

scorelist.sort()

scores = deque(scorelist)
for i in range(int(people)):
    scores.popleft()
    scores.pop()

print(makeround(sum(scores)/len(scores)) if scores else 0)