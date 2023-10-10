eyes = sorted(list(map(int, input().split())))
dice = [0 for _ in range(7)]
for eye in eyes: dice[eye] += 1

for i in range(7):
    if dice[i] == 3:
        print(10000 + (i*1000))
    if dice[i] == 2:
        print(1000 + (i*100))
if max(dice) == 1: print(eyes[2]*100)