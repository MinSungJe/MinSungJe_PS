N = int(input())
value = sum(list(map(int, input().split())))
print('yes' if value % 3 == 0 else 'no')