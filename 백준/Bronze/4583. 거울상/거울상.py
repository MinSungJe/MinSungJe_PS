# 거울상 초기값 선언
mirror = {
    'b': 'd',
    'd': 'b',
    'i': 'i',
    'o': 'o',
    'p': 'q',
    'q': 'p',
    'v': 'v',
    'w': 'w',
    'x': 'x'
}

# 입력부
while True:
    word = input()
    if word == '#': break

    # 거울상 찾기
    result = ''
    for i in range(len(word)-1, -1, -1):
        letter = word[i]
        if not letter in mirror.keys():
            result = 'INVALID'
            break
        result += mirror[letter]
    
    print(result)