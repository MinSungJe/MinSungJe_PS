def solution(answers):
    answer = []
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == ans1[i%5]: scores[0] += 1
        if answers[i] == ans2[i%8]: scores[1] += 1
        if answers[i] == ans3[i%10]: scores[2] += 1
    
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score: answer.append(i+1)
        
    return answer