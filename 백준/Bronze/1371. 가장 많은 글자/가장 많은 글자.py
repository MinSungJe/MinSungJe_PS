letters = [0 for _ in range(123)]

while True:
    try:
        sentence = input()
        for letter in sentence: letters[ord(letter)] += 1
    except: break

answer = ''
max_count = max(letters[97:])
for letter_index in range(97, 123):
    if letters[letter_index] == max_count: answer += chr(letter_index)

print(answer)