num = int(input())
result = 0
for i in reversed(range(0,(num//5)+1)):
    if (num-i*5) % 3 == 0:
        result += i
        result += ((num-i*5)//3)
        break

if result == 0:
    print(-1)
else:
    print(result)