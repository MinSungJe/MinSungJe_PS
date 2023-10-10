num = int(input())
letter = input()

idx = 0
sum = 0

for i in letter:
    sum += (ord(i)-96)*(31**idx)
    idx += 1

print(sum%1234567891)