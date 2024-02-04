# 입력부
S = input()
T = input()

def DFS(letter):
    result = 0

    if len(letter) == len(S): # S와 길이가 같아짐
        if letter == S: return 1
        else: return 0

    if letter[-1] == 'A': # 첫 번째 조건 성립
        result = result or DFS(letter[:-1])
    
    if letter[0] == 'B': # 두 번째 조건 성립
        new_letter = ''
        for i in range(len(letter)-1, 0, -1): new_letter += letter[i]
        result = result or DFS(new_letter)

    return result

# 출력부
print(DFS(T))