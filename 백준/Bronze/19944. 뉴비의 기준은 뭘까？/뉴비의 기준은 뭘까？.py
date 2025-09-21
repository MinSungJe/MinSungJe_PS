N, M = map(int, input().split())
answer = 'TLE!'
if M == 1 or M == 2: answer = 'NEWBIE!'
elif M <= N: answer = 'OLDBIE!'
print(answer)