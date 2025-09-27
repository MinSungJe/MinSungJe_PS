N = int(input())
result = list(map(int, input().split()))

answer = 0
streak = 0
for score in result:
    if score == 0: streak = 0
    else:
        streak += 1
        answer += streak
print(answer)