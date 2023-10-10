T = int(input())
for tc in range(1,T+1):
    OXs = input()
    sq = 0
    score = 0
    for i in OXs:
        if i == 'O':
            sq += 1
            score += sq
        else:
            sq = 0
    print(score)