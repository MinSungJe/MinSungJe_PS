# 입력부
N = int(input())
scores = list(map(int, input().split()))

# 누적합 구하기
sumlist = [0 for _ in range(N)]
sumlist[0] = scores[0]
for i in range(1, N):
    sumlist[i] = sumlist[i-1] + scores[i]
sumlist = [0] + sumlist

# 최솟값 배열 구하기
minlist = [0 for _ in range(N)]
minlist[N-1] = scores[N-1]
for i in range(N-2, -1, -1):
    minlist[i] = min(minlist[i+1], scores[i])

# 최대 점수 구하기
max_score = 0
for i in range(N-1):
    score = (sumlist[N] - sumlist[i] - minlist[i]) / (N-i-1)
    max_score = max(score, max_score)

# 최대 점수 조합 구하기
answer = []
for i in range(1, N-1):
    score = (sumlist[N] - sumlist[i] - minlist[i]) / (N-i-1)
    if score == max_score: answer.append(i)

# 출력부
for result in answer: print(result)