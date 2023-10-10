a = int(input())
b = int(input())
c = int(input())
num = a*b*c
numlist = [0] * 10

for letter in str(num):
    for j in range(10):
        if str(j) == letter:
            numlist[j] += 1

for i in range(10):
    print(numlist[i])