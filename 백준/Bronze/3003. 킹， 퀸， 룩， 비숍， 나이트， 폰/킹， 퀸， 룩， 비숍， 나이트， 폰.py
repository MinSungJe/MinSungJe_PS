chessset = [1,1,2,2,2,8]

inputset = list(map(int,input().split()))
resultset = [0,0,0,0,0,0]
for i in range(6):
    resultset[i] = chessset[i] - inputset[i]

print(*resultset)