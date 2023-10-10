num = int(input())
for i in range(num):
    for j in range(num):
        print(' ' if num-j-1 > i else '*', end = '')
    print('')