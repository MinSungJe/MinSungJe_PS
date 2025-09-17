# 입력부
K = input()

# 숫자로 변환
letter_count_map = {
    'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':3,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':3,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':2,'X':2,'Y':2,'Z':1
}
def get_letter_count(letter): return letter_count_map[letter]
letter_counts = list(map(get_letter_count, list(K)))

# 길이가 1이 될 때까지 계산
while len(letter_counts) > 1:
    temp = []
    for i in range(0, len(letter_counts), 2):
        if i+1 >= len(letter_counts): temp.append(letter_counts[i])
        else: temp.append((letter_counts[i] + letter_counts[i+1]) % 10)
    letter_counts = temp

# 출력부
answer = "I'm a winner!" if letter_counts[0] % 2 == 1 else "You're the winner?"
print(answer)