# 입력부
scores = [list(map(int, input().split())) for _ in range(5)]

# 우승자 가리기
winner = 0
max_score = 0
for i in range(5):
    value = sum(scores[i])
    if value > max_score:
        winner = i+1
        max_score = value

# 출력부
print(winner, max_score)