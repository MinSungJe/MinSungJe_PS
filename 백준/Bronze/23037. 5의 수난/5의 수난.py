numbers = input()

result = 0
for i in range(5):
    result += int(numbers[i]) ** 5
print(result)