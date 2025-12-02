# 펠린드롭인지 확인
def isPalin(word):
    result = True
    L = len(word)
    for i in range(L//2):
        if word[i] != word[L-1-i]: result = False
    
    return result


# TC
T = int(input())
for _ in range(T):
    N = int(input())
    words = [input() for _ in range(N)]

    # 단어 조합
    answer = 0
    for i in range(N):
        for j in range(N):
            if i == j: continue
            word = words[i] + words[j]
            if not isPalin(word): continue
            answer = word
            break

        if answer != 0: break
    
    # 출력부
    print(answer)