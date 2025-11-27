import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
marathoners = {}
marathoner_name = set()

for _ in range(N):
    name = input()
    if not name in marathoner_name:
        marathoners[name] = 1
        marathoner_name.add(name)
    else: marathoners[name] += 1
    
for _ in range(N-1):
    name = input()
    marathoners[name] -= 1

answer = ''
for name, value in marathoners.items():
    if value != 0: answer = name
print(answer)