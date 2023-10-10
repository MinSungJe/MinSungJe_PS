letter = input()
result = ''
for i in letter:
    if i.isupper():
        result += i.lower()
    else:
        result += i.upper()
print(result)