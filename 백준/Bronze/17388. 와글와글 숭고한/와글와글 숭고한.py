score = list(map(int, input().split()))
if sum(score) >= 100: print('OK')
else:
    if min(score) == score[0]: print('Soongsil')
    if min(score) == score[1]: print('Korea')
    if min(score) == score[2]: print('Hanyang')