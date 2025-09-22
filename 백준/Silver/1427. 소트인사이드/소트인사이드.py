numbers = list(map(int, list(input())))
numbers.sort(reverse=True)
answer = ''.join(list(map(str, numbers)))
print(answer)