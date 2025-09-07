month = int(input())
day = int(input())
answer = 'Special'
if month == 1: answer = 'Before'
if month >= 3: answer = 'After'
if month == 2:
    if day < 18: answer = 'Before'
    if day > 18: answer = 'After'
print(answer)