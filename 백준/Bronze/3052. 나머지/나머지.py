rests = []
for i in range(10):
    num = int(input())
    if (num % 42) not in rests:
        rests.append(num % 42)
print(len(rests))