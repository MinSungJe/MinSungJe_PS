N, M = map(int, input().split())
Map = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    for X in range(X1-1,X2):
        for Y in range(Y1-1,Y2):
            Map[X][Y] += 1

count = 0
for i in range(100):
    for j in range(100):
        if Map[i][j] > M: count += 1

print(count)