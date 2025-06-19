scores = [int(input()) for _ in range(8)]
high_scores = sorted(scores)[3:]

answer = sum(high_scores)
answer_idx = []
for high_score in high_scores:
    for i in range(8):
        if high_score == scores[i]:
            answer_idx.append(i+1)
            break

answer_idx.sort()

print(answer)
print(*answer_idx)