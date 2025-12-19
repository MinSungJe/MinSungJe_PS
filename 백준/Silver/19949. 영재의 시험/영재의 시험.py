# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
answers = list(map(int, input().split()))

# 전역변수 선언
answer = 0

# DFS
def DFS(idx, numbers, correct):
    global answer

    # 결과 확인
    if idx >= 10:
        if correct >= 5: answer += 1
        return
    
    # 다음 탐색
    for value in range(1, 6):
        if idx >= 2:
            if numbers[idx-1] == numbers[idx-2] and numbers[idx-1] == value: continue
        if value == answers[idx]: DFS(idx+1, numbers+[value], correct+1)
        else: DFS(idx+1, numbers+[value], correct)

# 함수 호출
DFS(0, [], 0)

# 출력부
print(answer)