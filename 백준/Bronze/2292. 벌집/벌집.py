target = int(input())

result = 1
room =  1

while 1:
    if room >= target:
        break
    else:
        room += 6 * result
        result += 1

print(result)