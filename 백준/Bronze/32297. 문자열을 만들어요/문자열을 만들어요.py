N = int(input())
word = input()

answer = 'NO'
for i in range(0, N-3):
    if word[i:i+4] == 'gori': answer = 'YES'
        
print(answer)