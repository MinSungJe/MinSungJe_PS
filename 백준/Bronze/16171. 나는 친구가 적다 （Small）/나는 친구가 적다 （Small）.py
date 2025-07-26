letter = input()
word = input()

password = ''
for w in letter:
    if w in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: continue
    password += w

answer = 0
for i in range(len(password) - len(word) + 1):
    if password[i:i+len(word)] == word: answer = 1
        
print(answer)