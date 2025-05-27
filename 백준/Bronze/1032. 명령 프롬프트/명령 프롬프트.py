# 입력부
N = int(input())
result = ''
for _ in range(N):
    word = input()
    if result == '':
        result = word
        continue
    L = len(word)

    for i in range(L):
        if result[i] == '?': continue
        if result[i] != word[i]:
            result = result[:i] + '?' + result[i+1:]
    
print(result)