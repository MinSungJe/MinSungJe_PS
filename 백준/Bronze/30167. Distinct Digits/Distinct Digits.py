l, r = map(int, input().split())
answer = -1
for number in range(l, r+1):
    number_set = set(str(number))
    if len(number_set) == len(str(number)):
        answer = number
        break
print(answer)