num = int(input())
llist = []
for i in range(num):
    letter = input()
    if letter not in llist:
        llist.append(letter)
llist.sort()
llist.sort(key=len)
for i in range(len(llist)):
    print(llist[i])