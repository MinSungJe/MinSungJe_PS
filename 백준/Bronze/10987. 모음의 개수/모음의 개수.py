letter = input()
answer = 0
for l in letter:
    if l in ['a', 'e', 'i', 'o', 'u']: answer += 1
print(answer)