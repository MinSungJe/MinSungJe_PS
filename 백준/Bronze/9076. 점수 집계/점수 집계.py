N = int(input())
for _ in range(N):
    scores = list(map(int, input().split()))
    scores.sort()
    
    if scores[3] - scores[1] >= 4:
        print('KIN')
        continue
    print(sum(scores[1:4]))