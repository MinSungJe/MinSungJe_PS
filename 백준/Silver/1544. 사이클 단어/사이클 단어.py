# 입력부
N = int(input())
words = list(input() for _ in range(N))

# 글자 바꾸기
def rotateWord(word):
    return word[1:] + word[0]

# 개수 세기
result = 0
while words:
    result += 1
    target = words.pop()
    
    # 글자 하나씩 돌려가며 제거
    for _ in range(len(target)):
        target = rotateWord(target)
        while target in words: words.remove(target)

# 출력부
print(result)