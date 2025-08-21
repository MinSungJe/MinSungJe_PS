def Rev(number):
    number_string = str(number)
    return int(number_string[::-1])

X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))