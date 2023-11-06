N = int(input())
word = input()
alphabet = dict()
answer = True

for letter in word[:N//2]+word[N//2+N%2:]:
    if letter in alphabet.keys(): alphabet[letter] += 1
    else: alphabet[letter] = 1

for value in alphabet.values():
    if value % 2 != 0:
        answer = False
        break

print("Yes" if answer else "No")