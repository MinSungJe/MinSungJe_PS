letter = input()
result = ''
cambridge = ['C','A','M','B','R','I','D','G','E']
for i in range(len(letter)):
    if not letter[i] in cambridge: result += letter[i]
print(result)