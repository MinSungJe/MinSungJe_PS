from collections import deque

num = int(input())
cards = deque([i for i in range(1,num+1)])

for i in range(num-1):
    cards.popleft()
    cards.rotate(-1)

print(*cards)