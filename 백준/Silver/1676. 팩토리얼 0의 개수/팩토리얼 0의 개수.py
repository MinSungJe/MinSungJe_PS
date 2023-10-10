values = [0] * 501

def factorial(idx):
    if idx == 0 or idx == 1:
        return 1
    if values[idx] != 0:
        return values[idx]
    if values[idx] == 0:
        values[idx] = idx * factorial(idx-1)
        return values[idx]
    
count = 0
for i in reversed(str(factorial(int(input())))):
    if i == '0':
        count += 1
    else:
        break

print(count)