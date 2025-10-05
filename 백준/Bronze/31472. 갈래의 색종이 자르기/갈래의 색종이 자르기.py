W = int(input())
line = 0
for i in range(2, 201, 2):
    if W == i * (i // 2):
        line = i
        break
answer = 4 * line
print(answer)