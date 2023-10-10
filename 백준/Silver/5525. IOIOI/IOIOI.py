N = int(input())
Pn = ''
flag = False
for i in range(2*N+1):
    if not flag:
        Pn += 'I'
        flag = True
    else:
        Pn += 'O'
        flag = False

M = int(input())
S = input()

count = 0

for i in range(M):
    if S[i] == 'I' and S[i:i+len(Pn)] == Pn:
        count += 1

print(count)