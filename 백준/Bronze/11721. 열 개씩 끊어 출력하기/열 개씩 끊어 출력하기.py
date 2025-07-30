sentence = input()
answer = list()
temp = list()
for letter in sentence:
    temp.append(letter)
    if len(temp) == 10:
        answer.append(''.join(temp))
        temp = list()

if len(temp) > 0: answer.append(''.join(temp))

for row in answer: print(row)