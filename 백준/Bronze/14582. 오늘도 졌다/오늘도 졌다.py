# 입력부
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

score1 = 0
score2 = 0

# 역전 당했는지 확인
overTeam2 = False
for i in range(9):
    score1 += team1[i]
    
    # 앞서나간 적이 있는지 확인
    if score1 > score2: overTeam2 = True

    score2 += team2[i]

# 출력부
answer = 'Yes' if overTeam2 and score1 < score2 else 'No'
print(answer)