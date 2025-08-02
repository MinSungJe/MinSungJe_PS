N = int(input())
names = [input() for _ in range(N)]

names.sort()
for name in names:
    if len(name) == 3:
        print(name)
        break