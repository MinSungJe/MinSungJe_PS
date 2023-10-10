letter = input()
idx = int(input())
for i in enumerate(letter, start=1):
    if i[0] == idx:
        print(i[1])
    
    