N = int(input())

row = (N // 2) + N % 2 + 1
column = (N // 2) + 1

print(row * column)