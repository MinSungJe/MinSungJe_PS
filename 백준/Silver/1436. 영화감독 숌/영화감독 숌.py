title = int(input())

num = 99
count = 0
while True:
    num += 1
    if "666" in str(num):
        count += 1
    if count == title:
        break

print(num)