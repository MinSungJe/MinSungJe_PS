N, M = map(int, input().split())

bread = list(input() for _ in range(N))

for row in bread:
    print(row[::-1])