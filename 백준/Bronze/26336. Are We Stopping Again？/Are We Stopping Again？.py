t = int(input())
for _ in range(t):
    m, g, f = map(int, input().split())

    result = [0 for _ in range(m)]
    for i in range(g, m, g):
        result[i] = 1
    for i in range(f, m, f):
        result[i] = 1

    print(m, g, f)
    print(sum(result))