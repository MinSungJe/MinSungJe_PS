N = int(input())
numbers = [0 for _ in range(21)]
numbers[1] = 1
for i in range(2, 21):
    numbers[i] = numbers[i-1]+numbers[i-2]
    
print(numbers[N])