answer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for _ in range(10):
    a, b = map(int, input().split())

    temp = answer[:]
    length = b - a + 1
    for i in range(length):
        answer[a-1+i] = temp[b-1-i]


print(*answer)