N = int(input())
tulips = list(map(int, input().split()))

print(15000 - len(set(tulips)))