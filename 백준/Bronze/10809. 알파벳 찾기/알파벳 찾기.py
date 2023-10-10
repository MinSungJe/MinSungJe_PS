letter = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
result = [-1] * 26
for i,a in enumerate(alphabets):
    dict[a] = i

for i in range(len(letter)):
    if result[dict[letter[i]]] == -1:
        result[dict[letter[i]]] = i

print(*result)