# 입력부
N, mood = map(int, input().split())
pospos, posneg, negpos, negneg = map(float, input().split())

# 결과 계산
pos, neg = (1-mood), mood
for _ in range(N):
    prev_pos = pos
    pos = prev_pos * pospos + (1-prev_pos) * negpos
    neg = prev_pos * posneg + (1-prev_pos) * negneg

# 출력부
print(int(pos * 1000))
print(int(neg * 1000))